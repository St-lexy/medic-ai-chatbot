# 🩺 MediC - AI Medical Consultant Chatbot

An intelligent healthcare chatbot powered by Large Language Models (LLMs) and AutoGen framework. MediC provides empathetic, accurate, and safe health information while maintaining strict medical safety protocols and user-friendly conversational interface.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![AutoGen](https://img.shields.io/badge/autogen-latest-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Project Overview

MediC (Medical Consultant) is an AI-powered conversational agent that serves as a friendly medical information assistant. Built with Microsoft's AutoGen framework and Groq's LLM API, it provides reliable health guidance while prioritizing user safety through comprehensive disclaimers and intelligent response filtering.

### Key Features

✅ **Conversational AI Interface** - Natural, empathetic dialogue with users  
✅ **Safety-First Design** - Built-in medical disclaimers and safety protocols  
✅ **Urgency Classification** - Categorizes health concerns (Emergency 🚨, Urgent ⚠️, Routine 📅, Wellness 🌱)  
✅ **Conversation History** - Maintains context across multiple queries  
✅ **Quick Action Buttons** - Pre-defined health topics for easy access  
✅ **Professional Medical Persona** - Simulates Dr. Williams, a knowledgeable AI consultant  
✅ **Streamlit UI** - Clean, intuitive web interface  

## 🎯 Problem Statement

Healthcare information can be:
- Overwhelming and difficult to understand
- Inaccessible outside medical facilities
- Confusing due to medical jargon
- Time-consuming to research properly

**MediC bridges this gap** by providing:
- Instant, 24/7 health information access
- Plain-language explanations
- Preliminary guidance before doctor visits
- Educational health content

## 🏗️ Technical Architecture

### System Design

```
User Input (Streamlit UI)
    ↓
AutoGen User Agent (Patient)
    ↓
AutoGen Conversable Agent (Dr. Williams)
    ↓
Groq API (LLM: openai/gpt-oss-20b)
    ↓
Response Processing & Safety Filtering
    ↓
Streamlit Display (with disclaimers)
```

### Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Framework**: Microsoft AutoGen (Multi-agent conversation framework)
- **LLM Provider**: Groq API (High-performance inference)
- **Model**: OpenAI GPT-based model (gpt-oss-20b)
- **Language**: Python 3.8+

### Core Components

**1. Medical Consultant Agent (Dr. Williams)**
- Equipped with comprehensive medical knowledge
- Programmed with safety-first protocols
- Responds with empathy and clarity
- Never provides diagnosis or prescriptions

**2. User Agent (Patient)**
- Represents the user in the conversation
- Handles input formatting
- Manages conversation flow

**3. Safety System**
- Pre-response disclaimers
- Post-response warnings
- Emergency detection keywords
- Professional referral recommendations

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8 or higher
pip (Python package manager)
Groq API key (free tier available)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/St-Lexy/medic-ai-chatbot.git
cd medic-ai-chatbot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
# Create a .env file
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

Or set environment variable directly:
```bash
# Linux/Mac
export GROQ_API_KEY="your_groq_api_key_here"

# Windows
set GROQ_API_KEY=your_groq_api_key_here
```

4. **Run the application**
```bash
streamlit run medic_chatbot.py
```

5. **Access the app**
- Open your browser
- Navigate to `http://localhost:8501`

### Getting a Groq API Key

1. Visit [Groq Cloud](https://console.groq.com/)
2. Sign up for a free account
3. Navigate to API Keys section
4. Generate a new API key
5. Copy and use in your `.env` file

**Note**: Groq offers free tier with generous limits, making it perfect for development and demos.

## 📋 Usage Guide

### Basic Workflow

1. **Ask a Health Question**
   - Type your symptoms or health concern
   - Be specific about duration and severity
   - Example: "I've been having headaches for the past week"

2. **Review MediC's Response**
   - Read the professional analysis
   - Check urgency classification
   - Note any wellness tips provided

3. **Follow Up (Optional)**
   - Ask clarifying questions
   - Request more details
   - Context is maintained in conversation history

4. **Take Action**
   - Follow general wellness advice
   - Consult healthcare professional if recommended
   - Seek emergency care if flagged as urgent

### Quick Health Topics

Use sidebar buttons for instant information on:
- 🤒 Fever & Symptoms
- 💊 Headaches
- 😴 Sleep Issues
- 🏃‍♂️ Exercise & Health

### Example Interactions

**Query**: "I've been having headaches for the past week. They're worse in the morning and I feel nauseous."

**MediC Response Structure**:
1. Professional acknowledgment
2. Clarifying questions (if needed)
3. Plain-language explanation
4. Urgency assessment (⚠️ Urgent in this case)
5. Safe wellness tips
6. Recommendation to see a doctor
7. Safety disclaimer

## 🛡️ Safety & Ethics

### Built-in Safety Measures

**Medical Disclaimers**:
- Displayed prominently on app launch
- Repeated after every consultation
- Clear statement: "Not medical advice"

**Response Filtering**:
- Never provides exact medication dosages
- Avoids definitive diagnoses
- Always recommends professional consultation for serious concerns

**Emergency Handling**:
- Detects emergency keywords
- Immediately recommends seeking medical care
- Provides clear urgency classification

### Ethical Considerations

✅ Transparency about AI limitations  
✅ Clear distinction from real medical professionals  
✅ Privacy-conscious (no data stored without consent)  
✅ Accessible and inclusive language  
✅ Focus on education, not treatment  

## 📁 Project Structure

```
medic-ai-chatbot/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── medic_chatbot.py            # Main Streamlit application
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore file (includes .env)
├── assets/                     # Images and resources
│   ├── demo_screenshot.png
│   └── architecture_diagram.png
├── docs/                       # Additional documentation
│   ├── SETUP_GUIDE.md
│   └── API_DOCUMENTATION.md
└── tests/                      # Test files (optional)
    └── test_chatbot.py
```

## 🎓 Key Learnings & Technical Insights

### 1. **Multi-Agent Conversation Framework**
- AutoGen simplifies agent-to-agent communication
- Separation of concerns (user agent vs consultant agent)
- Easier to manage conversation flow and context

### 2. **Prompt Engineering for Safety**
- System message defines behavior boundaries
- Structured response format ensures consistency
- Safety rules embedded in agent instructions

### 3. **Streamlit for Rapid Prototyping**
- Quick UI development with minimal code
- Built-in session state management
- Easy deployment options

### 4. **LLM API Integration**
- Groq provides fast inference speeds
- OpenAI-compatible API makes switching models easy
- Cost-effective for development and demos

### 5. **Healthcare AI Challenges**
- Balancing helpfulness with safety
- Avoiding liability while providing value
- Managing user expectations
- Ensuring accessibility

## 🔮 Future Enhancements

### Planned Features

- [ ] **RAG Integration** - Connect to medical knowledge bases (PubMed, medical textbooks)
- [ ] **Multi-language Support** - Reach non-English speakers
- [ ] **Voice Input/Output** - Accessibility for visually impaired users
- [ ] **Symptom Checker** - Structured questionnaire flow
- [ ] **Medical History Tracking** - Optional user profiles (with consent)
- [ ] **Doctor Finder Integration** - Connect users to real healthcare providers
- [ ] **Export Consultation** - Save conversations as PDF for doctor visits
- [ ] **Analytics Dashboard** - Track common health concerns and trends

### Technical Improvements

- [ ] Add unit tests for agent responses
- [ ] Implement response caching for common queries
- [ ] Add rate limiting for API calls
- [ ] Deploy to cloud (Streamlit Cloud, Heroku, AWS)
- [ ] Add database for conversation persistence
- [ ] Implement user authentication (optional)
- [ ] Add A/B testing for prompt variations
- [ ] Create mobile-responsive design

## 📊 Performance & Metrics

### Response Quality
- **Average Response Time**: ~2-3 seconds
- **User Satisfaction**: Subjective (need user testing)
- **Safety Compliance**: 100% (all responses include disclaimers)

### System Performance
- **API Latency**: Depends on Groq service (~1-2s typical)
- **UI Responsiveness**: Fast (Streamlit is lightweight)
- **Scalability**: Limited by API rate limits

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **Streamlit** - Web application framework
- **AutoGen** - Multi-agent conversation framework (Microsoft)
- **Groq API** - High-performance LLM inference
- **OpenAI-compatible Models** - Language understanding

## ⚠️ Important Disclaimers

**FOR EDUCATIONAL AND INFORMATIONAL PURPOSES ONLY**

This application:
- ❌ Is NOT a substitute for professional medical advice
- ❌ Does NOT diagnose medical conditions
- ❌ Does NOT prescribe treatments or medications
- ❌ Should NOT be used in medical emergencies

**Always consult qualified healthcare professionals for medical concerns.**

In case of emergency: Call emergency services or go to the nearest hospital immediately.

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

### Development Guidelines
- Maintain safety-first approach
- Add tests for new features
- Update documentation
- Follow Python PEP 8 style guide

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Microsoft AutoGen** - For the multi-agent framework
- **Groq** - For fast LLM inference API
- **Streamlit** - For the web framework
- **Medical community** - For inspiration and safety guidelines

## 👤 Author

**Amusan Olanrewaju Stephen**
- GitHub: [@St-Lexy](https://github.com/St-Lexy)
- LinkedIn: [olanrewaju-amusan](https://linkedin.com/in/olanrewaju-amusan)
- Email: amusanolanrewaju420@gmail.com
- Portfolio: [st-lexy.github.io](https://st-lexy.github.io)

## 📞 Support

For questions, issues, or suggestions:
- Open an [Issue](https://github.com/St-Lexy/medic-ai-chatbot/issues)
- Email: amusanolanrewaju420@gmail.com

## 🔗 Related Resources

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Groq API Docs](https://console.groq.com/docs)
- [Responsible AI Guidelines](https://www.microsoft.com/en-us/ai/responsible-ai)

---

⭐ **If you find this project useful, please consider giving it a star!**

💙 **Remember: This is an educational tool. Always prioritize real healthcare professionals for medical decisions.**