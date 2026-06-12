"""JanaSeva AI Streamlit application powered by Groq."""

import os
from typing import Any, Dict

from dotenv import load_dotenv
import streamlit as st
from groq import Groq, GroqError

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(page_title="JanaSeva AI", page_icon="📱", layout="wide")

# ==================================
# CUSTOM CSS
# ==================================

st.markdown(
    """
<style>

.stApp {
    background-color: #0b1220;
}

section[data-testid="stSidebar"] {
    background-color: #1a1f2e;
}

h1, h2, h3, h4, p, label {
    color: white !important;
}

.stTextInput input {
    background-color: #1f2937 !important;
    color: white !important;
    border: 1px solid #4b5563 !important;
    border-radius: 8px !important;
}

.stTextInput input::placeholder {
    color: #d1d5db !important;
}

.stButton > button {
    background-color: #2563eb !important;
    color: white !important;
    border-radius: 8px !important;
    border: none !important;
    font-weight: bold !important;
}

.stButton > button:hover {
    background-color: #1d4ed8 !important;
    color: white !important;
}

.block-container {
    padding-top: 2rem;
}

</style>
""",
    unsafe_allow_html=True,
)

# ==================================
# LOAD API KEY
# ==================================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    try:
        secrets = getattr(st, "secrets", None)
        if secrets is not None:
            GROQ_API_KEY = secrets.get("GROQ_API_KEY")
    except Exception:
        GROQ_API_KEY = None

if not GROQ_API_KEY:
    st.error("❌ API key not configured.")
    st.stop()

# ==================================
# GROQ CLIENT
# ==================================

try:
    client = Groq(api_key=GROQ_API_KEY)
except GroqError as error:
    st.error(f"❌ Failed to initialize AI service: {error}")
    st.stop()

# ==================================
# LANGUAGE SELECTOR
# ==================================

language = st.sidebar.selectbox("🌐 Language", ["English", "తెలుగు", "हिन्दी"])

translations: Dict[str, Dict[str, Any]] = {
    "English": {
        "title": "JanaSeva AI",
        "home": "🏠 Home",
        "assistant": "🤖 Assistant",
        "navigation": "Navigation",
        "welcome": "Welcome to JanaSeva AI",
        "about": "JanaSeva AI helps citizens with Aadhaar, PAN, Passport, Ration Card, Certificates, Government Schemes and more.",
        "services": "Available Services",
        "question": "Ask your civic question",
        "button": "Generate Response",
        "response": "Response",
        "warning": "Please enter a question.",
        "thinking": "Thinking...",
        "examples_title": "Example Questions",
        "service_list": [
            "Aadhaar Services",
            "PAN Card Services",
            "Passport Services",
            "Driving Licence",
            "Ration Card",
            "Income Certificate",
            "Caste Certificate",
            "Birth Certificate",
            "Government Schemes",
            "MeeSeva Services",
        ],
        "examples": [
            "How to update Aadhaar card?",
            "How to apply for PAN card?",
            "How to get income certificate?",
            "How to apply for passport?",
            "How to apply for ration card?",
        ],
    },
    "తెలుగు": {
        "title": "జనసేవ AI",
        "home": "🏠 హోమ్",
        "assistant": "🤖 సహాయకుడు",
        "navigation": "నావిగేషన్",
        "welcome": "జనసేవ AI కి స్వాగతం",
        "about": "ఆధార్, పాన్, పాస్‌పోర్ట్, రేషన్ కార్డు, ప్రభుత్వ పథకాలు మరియు ఇతర సేవల సమాచారం పొందండి.",
        "services": "అందుబాటులో ఉన్న సేవలు",
        "question": "మీ ప్రశ్న అడగండి",
        "button": "సమాధానం పొందండి",
        "response": "సమాధానం",
        "warning": "దయచేసి ఒక ప్రశ్న నమోదు చేయండి.",
        "thinking": "ఆలోచిస్తోంది...",
        "examples_title": "ఉదాహరణ ప్రశ్నలు",
        "service_list": [
            "ఆధార్ సేవలు",
            "పాన్ కార్డ్ సేవలు",
            "పాస్‌పోర్ట్ సేవలు",
            "డ్రైవింగ్ లైసెన్స్",
            "రేషన్ కార్డ్",
            "ఆదాయ ధృవీకరణ పత్రం",
            "కుల ధృవీకరణ పత్రం",
            "జనన ధృవీకరణ పత్రం",
            "ప్రభుత్వ పథకాలు",
            "మీ సేవ సేవలు",
        ],
        "examples": [
            "ఆధార్ కార్డ్‌ను ఎలా అప్డేట్ చేయాలి?",
            "పాన్ కార్డ్‌కు ఎలా దరఖాస్తు చేయాలి?",
            "ఆదాయ ధృవీకరణ పత్రం ఎలా పొందాలి?",
            "పాస్‌పోర్ట్‌కు ఎలా దరఖాస్తు చేయాలి?",
            "రేషన్ కార్డ్‌కు ఎలా దరఖాస్తు చేయాలి?",
        ],
    },
    "हिन्दी": {
        "title": "जनसेवा AI",
        "home": "🏠 होम",
        "assistant": "🤖 सहायक",
        "navigation": "नेविगेशन",
        "welcome": "जनसेवा AI में आपका स्वागत है",
        "about": "आधार, पैन, पासपोर्ट, राशन कार्ड, सरकारी योजनाओं और अन्य सेवाओं की जानकारी प्राप्त करें।",
        "services": "उपलब्ध सेवाएं",
        "question": "अपना प्रश्न पूछें",
        "button": "उत्तर प्राप्त करें",
        "response": "उत्तर",
        "warning": "कृपया एक प्रश्न दर्ज करें।",
        "thinking": "सोच रहा है...",
        "examples_title": "उदाहरण प्रश्न",
        "service_list": [
            "आधार सेवाएं",
            "पैन कार्ड सेवाएं",
            "पासपोर्ट सेवाएं",
            "ड्राइविंग लाइसेंस",
            "राशन कार्ड",
            "आय प्रमाण पत्र",
            "जाति प्रमाण पत्र",
            "जन्म प्रमाण पत्र",
            "सरकारी योजनाएं",
            "मी सेवा सेवाएं",
        ],
        "examples": [
            "आधार कार्ड कैसे अपडेट करें?",
            "पैन कार्ड के लिए आवेदन कैसे करें?",
            "आय प्रमाण पत्र कैसे प्राप्त करें?",
            "पासपोर्ट के लिए आवेदन कैसे करें?",
            "राशन कार्ड के लिए आवेदन कैसे करें?",
        ],
    },
}

t = translations[language]

# ==================================
# SIDEBAR
# ==================================

st.sidebar.title("📌 " + str(t["title"]))

page = st.sidebar.radio(str(t["navigation"]), [str(t["home"]), str(t["assistant"])])
# ==================================
# HOME PAGE
# ==================================

if page == t["home"]:

    st.title("📱 " + t["title"])

    st.subheader(t["welcome"])

    st.write(t["about"])

    st.subheader(t["services"])

    for service in t["service_list"]:
        st.markdown(f"- {service}")

    st.markdown(f"### {t['examples_title']}")

    for question in t["examples"]:
        st.markdown(f"- {question}")
# ==================================
# AI FUNCTION
# ==================================


def get_response(question: str) -> str:
    """Generate an answer from the Groq chat completion API."""

    system_prompt = f"""
You are JanaSeva AI.

Answer completely in {language}.

For government-related questions provide:

1. Introduction
2. Online Method (step-by-step)
3. Offline Method (step-by-step)
4. Required Documents
5. Fees
6. Processing Time
7. Official Website
8. Important Notes

Use simple language.
Do not mix languages.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
            temperature=0.5,
            max_tokens=1500,
        )

        return str(response.choices[0].message.content)
    except (IndexError, AttributeError, TypeError, GroqError) as error:
        return f"❌ Error: {error}"


# ==================================
# ASSISTANT PAGE
# ==================================

if page == t["assistant"]:

    st.title("🤖 " + t["title"])

    user_question = st.text_input(
        str(t["question"]),
        placeholder=str(t["examples"][0]),
    )

    if st.button(t["button"]):

        if not user_question.strip():
            st.warning(t["warning"])

        else:

            try:

                with st.spinner(t["thinking"]):

                    answer = get_response(user_question)

                st.markdown(f"### 📋 {t['response']}")
                st.success(answer)

            except Exception as error:
                st.error(f"Error: {error}")