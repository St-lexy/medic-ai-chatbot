import streamlit as st
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import os
groq_key = os.getenv("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")

# Page configuration
st.set_page_config(
    page_title="MediC - AI Medical Consultant",
    page_icon="🩺",
    layout="centered"
)

# System prompt
SYSTEM_PROMPT = """You are MediC, an AI medical consultant.
You help people understand their health concerns through natural, ongoing conversation.

🎯 YOUR APPROACH:
- Start with empathy and curiosity - understand their concern first
- Ask clarifying questions naturally (don't interrogate, just be curious)
- Explain things simply, one concept at a time
- Only assess urgency when you have enough context
- Keep responses conversational (3-5 short paragraphs max)
- Invite further questions - make people feel comfortable continuing

⚠️ SAFETY BOUNDARIES:
- Never diagnose specific conditions or prescribe medications
- For serious symptoms (severe pain, difficulty breathing, chest pain, sudden weakness, heavy bleeding), 
  immediately advise seeking emergency care
- When uncertain about severity, encourage professional evaluation
- You educate and guide, but don't replace doctors

✨ CONVERSATION STYLE:
- Warm and approachable, like talking to a knowledgeable friend
- Use analogies and examples to explain medical concepts
- Respond proportionally - brief questions get brief answers, complex concerns get depth
- Show you're listening by referencing what they've shared
- End with an opening, not a closing (e.g., "What else would you like to know?" or 
  "Does this help clarify things?")

🚨 URGENCY ASSESSMENT (only when you have enough context):
- 🚨 Emergency: Seek immediate care (be specific about why)
- ⚠️ Urgent: See a doctor within 24-48 hours
- 📅 Routine: Schedule an appointment when convenient
- 🌱 Wellness: General health optimization

Remember: You're having a conversation, not writing a medical report. 
Build trust through dialogue, not through comprehensive single responses."""

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm MediC, your AI medical consultant. I'm here to help answer your health questions and provide general guidance. How can I assist you today?"
        }
    ]

# Initialize AutoGen agents
if "assistant" not in st.session_state:
    try:
        config_list = [
            {
                "model":  "openai/gpt-oss-20b",
                "api_key": groq_key,
                "base_url": "https://api.groq.com/openai/v1",
                "tool_choice": "none",
            }
        ]
        
        st.session_state.assistant = AssistantAgent(
            name="MediC",
            system_message=SYSTEM_PROMPT,
            llm_config={
                "config_list": config_list,
                "temperature": 0.7,
            }
        )
        
        st.session_state.user_proxy = UserProxyAgent(
            name="Patient",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=0,
            code_execution_config=False,
        )
        
    except Exception as e:
        st.error(f"Error initializing agents: {str(e)}")
        st.session_state.assistant = None
        st.session_state.user_proxy = None
        
if st.session_state.assistant:
    st.session_state.assistant.reset()

# Header
col1, col2 = st.columns([8, 2])
with col1:
    st.title("🩺 MediC")
    st.caption("""*Hello 👋 I'm 🩺 MediC, your friendly medical consultant AI.
Think of me as a supportive guide you can talk to about your health, lifestyle, and wellness questions.
I'll explain things in simple terms, give useful tips, and let you know when it's important to see a real healthcare professional.
I'm here to make health information feel less intimidating.*""")
with col2:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "How can I help you 😁😷😁"
            }
        ]
        # Clear conversation history in agents
        if st.session_state.assistant:
            st.session_state.assistant.clear_history()
        if st.session_state.user_proxy:
            st.session_state.user_proxy.clear_history()
        st.rerun()

st.divider()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="👤" if message["role"] == "user" else "🩺"):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's on your mind? Share your symptoms, worries or question here 🙃"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    with st.chat_message("assistant", avatar="🩺"):
        message_placeholder = st.empty()
        
        if st.session_state.assistant is None or st.session_state.user_proxy is None:
            message_placeholder.error("⚠️ Agents not initialized. Please check your configuration.")
        else:
            try:
                st.session_state.user_proxy.initiate_chat(
                    st.session_state.assistant,
                    message=prompt,
                    clear_history=False 
                )
                
                last_message = st.session_state.assistant.last_message()
                
                if last_message and "content" in last_message:
                    full_response = last_message["content"]
                    message_placeholder.markdown(full_response)
                    
                    st.session_state.messages.append(
                        {"role": "assistant", "content": full_response}
                    )
                else:
                    message_placeholder.error("⚠️ No response received from assistant.")
                
            except Exception as e:
                message_placeholder.error(f"⚠️ Error: {str(e)}")

# Footer disclaimer
st.divider()
st.caption("⚠️ **Disclaimer:** This is for informational purposes only and not a substitute for professional medical advice. For emergencies, seek immediate medical care.")

# Sidebar with configuration info
with st.sidebar:
    st.header("💡 How to Use")
    st.markdown("""
    1. Ask one health question at a time
    2. Be specific about symptoms
    3. Get comprehensive response
    4. Ask follow-up questions if needed 
    5. **And always remember to consult healthcare professionals**
    """)
    
    st.divider()
    
    st.subheader("⚙️ Configuration")
    if st.session_state.assistant:
        st.session_state.assistant.reset()
        st.success("✓ Agents initialized")
    else:
        st.error("✗ Agents not initialized")
    
    st.divider()
    st.subheader("ℹ️ About MediC")
    st.write("MediC uses Open Source LLM (openai/gpt-oss-20b) and AutoGen to provide conversational medical guidance.")

    st.subheader("Features:")
    st.write("✅ Conversation history")
    st.write("✅ Context-aware responses")
    st.write("✅ Reset capability")
    st.write("✅ Multi-turn dialogue")

    st.write(f"Messages in history: {len(st.session_state.messages)}")


