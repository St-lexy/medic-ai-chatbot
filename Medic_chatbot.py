import streamlit as st
from autogen import ConversableAgent
import os

# Users should set: export GROQ_API_KEY="your_key_here"
os.environ["GROQ_API_KEY"] = "your GROQ_API_KEY here"

if not os.environ["GROQ_API_KEY"]:
    st.error("⚠️ GROQ_API_KEY environment variable not set. Please set it before running the app.")
    st.info("Set it using: export GROQ_API_KEY='your_groq_api_key_here'")
    st.stop()

llm_config = {
   "model":  "openai/gpt-oss-20b",
   "api_key": os.environ["GROQ_API_KEY"],
    "base_url": "https://api.groq.com/openai/v1",
    "tool_choice": "none",
}

st.set_page_config(
    page_title="Medical Consultant (🩺 MediC)",
    page_icon="🏥",
    layout="wide"
)

medical_consultant = ConversableAgent(
    "MediC",
    llm_config=llm_config,
    system_message = """
You are Dr. Williams, an AI medical consultant.
Your role is to respond to user health questions with empathy, clarity, and accurate general information.
Every user message should be treated as a patient concern or health-related question.

⚠️ SAFETY RULE (always follow):
- You are NOT a replacement for professional medical advice, diagnosis, or treatment.
- Never prescribe medications or provide exact dosages.
- For emergencies, go to your nearest healthcare centre or hospital immediately.
- When in doubt, recommend consulting a licensed healthcare provider.

🎯 HOW TO RESPOND:
1. **Acknowledge professionally**
2. **Ask clarifying questions** - when user's input is vague or incomplete.
3. **Educate in plain language** - explain the topic/symptoms clearly and simply
   (Use examples, analogies, or simple explanations instead of textbook jargon.).
4. **Assess urgency** - classify as Emergency 🚨, Urgent ⚠️, Routine 📅, or Wellness 🌱, and explain why.
5. **Offer safe wellness tips** - general self-care or preventive advice if relevant.
6. **End with a disclaimer** - remind that you are not a substitute for a real doctor.

✨ STYLE & TONE:
- Warm, conversational, and approachable - not textbook or robotic.
- Use short paragraphs, simple examples or analogies where helpful.
- Be concise but thorough (4-7 short sections is ideal).
- Always prioritize user safety and reassurance.
- Always keep safety first.

Remember: You educate and guide with kindness and clarity,
but you never diagnose, prescribe, or replace professional medical care.
"""
)

user_agent = ConversableAgent(
    "Patient",
    llm_config=False,
    human_input_mode="NEVER",
    code_execution_config=False,
)

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

st.title("🩺 MediC")
st.markdown('''*Hello 👋 I'm 🩺 MediC, your friendly medical consultant AI.
Think of me as a supportive guide you can talk to about your health, lifestyle, and wellness questions.
I'll explain things in simple terms, give useful tips, and let you know when it's important to see a real healthcare professional.
I'm here to make health information feel less intimidating.*
        ''')
st.markdown("---")

st.error("""
⚠️ **IMPORTANT MEDICAL DISCLAIMER** ⚠️

I can share reliable, easy to understand health information for general education and wellness support.

**But remember:**

- This is **not** medical advice, diagnosis, or treatment  
- I cannot prescribe medications or replace a qualified healthcare professional
- Always consult a licensed doctor or healthcare provider for any medical concerns, treatment decisions, or emergencies  
- If you ever feel you're experiencing a **medical emergency**, go to the nearest hospital right away

**Your safety always comes first 💙💙💙**
""")

with st.sidebar:
    st.header("💡 How to Use")
    st.markdown("""
    1. Ask one health question at a time
    2. Be specific about symptoms
    3. Get comprehensive response
    4. Ask follow-up questions as needed 
    5. Answer any clarifying questions I may have, while keeping your previous questions in context
    6. **Always consult healthcare professionals**
    """)

    # Quick action buttons for common questions
    st.markdown("---")
    st.header("🔍 Quick Health Topics")
    
    if st.button("🤒 Fever & Symptoms"):
        st.session_state.current_question = "What should I know about fever and when should I be concerned?"
        st.rerun()

    if st.button("💊 Headaches"):
        st.session_state.current_question = "I've been getting headaches frequently. What could be causing them and when should I see a doctor?"
        st.rerun()

    if st.button("😴 Sleep Issues"):
        st.session_state.current_question = "I'm having trouble sleeping well. What are some healthy sleep habits and when should I seek help?"
        st.rerun()

    if st.button("🏃‍♂️ Exercise & Health"):
        st.session_state.current_question = "How much exercise do I need for good health and what are safe ways to start exercising?"
        st.rerun()
    
    st.markdown("---")
    if st.button('🗑️ Clear All Questions'):
        st.session_state.conversation_history = []
        st.success("Conversation cleared!")
        st.rerun()

if st.session_state.conversation_history:
    st.subheader("📋 History:")
    for i, qa in enumerate(st.session_state.conversation_history):
        with st.container():
            st.markdown(f"**Question {i+1}:**")
            st.info(f"**You asked:** {qa['question']}")
            st.markdown("**🩺 MediC replied:**")
            st.success(qa['answer'])
            st.markdown("---")

st.markdown("---")
st.subheader("How can I help you 😁😷😁")
medical_question = st.text_area(
    "What's on your mind? Share your symptoms, worries or question here 🙃",
    placeholder="Example: I've been having headaches for the past week. They're worse in the morning and I feel nauseous. Should I be concerned?",
    height=100,
    key="current_question"
)

ask_button = st.button('🩺 Ask MediC', type="primary")

if ask_button and medical_question:
    with st.spinner("🔍 MediC is analyzing your question..."):
        try:
            # Create the consultation
            chat_result = user_agent.initiate_chat(
                medical_consultant, 
                message=medical_question,
                max_turns=1, 
                stream=True
            )
            
            consultant_response = ""
            for msg in chat_result.chat_history:
                if msg.get("name") == "MediC":
                    consultant_response = msg["content"]
                    break
            
            st.session_state.conversation_history.append({
                'question': medical_question,
                'answer': consultant_response
            })
            
            st.subheader("🏥 MediC Consultation:")
            st.success(consultant_response)
            
            st.warning("""
            **⚠️ IMPORTANT REMINDER:**
            This consultation is for educational purposes only. Please consult a real healthcare professional for proper medical advice.
            """)
            
            st.rerun()
                    
        except Exception as e:
            st.error(f"Error during consultation: {str(e)}")
            st.info("Please try again or consult a healthcare professional directly.")

elif ask_button and not medical_question:
    st.warning("Please enter your health question before consulting MediC.")

# Additional Resources
with st.expander("📚 Trusted Health Resources"):
    st.markdown("""
    **Reliable Health Information Sources:**
    - [WebMD](https://www.webmd.com/) - General health information
    - [Mayo Clinic](https://www.mayoclinic.org/) - Conditions and treatments  
    - [CDC](https://www.cdc.gov/) - Disease prevention and health promotion
    - [NIH](https://www.nih.gov/) - Medical research and health information
    
    **When to Seek Immediate Medical Care:**
    - Chest pain or pressure  •  Difficulty breathing  •  Severe bleeding
    - Signs of stroke  •  Loss of consciousness  •  Severe allergic reactions
    """)

st.markdown("---")
st.markdown("*Dr. Williams provides educational health information only. Always consult qualified healthcare professionals for medical advice.*")