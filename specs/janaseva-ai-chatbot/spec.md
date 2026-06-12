# JanaSeva AI Chatbot Feature Spec

## Problem
Citizens need a simple assistant to answer civic questions, explain government services, and recommend mobile apps.

## Solution
Build a Streamlit chatbot that uses the Groq API to respond to citizen queries about Aadhaar, ration cards, public services, and complaint processes.

## Users
- Citizens seeking civic guidance
- Developers reviewing chatbot behavior

## Requirements
- Load API key from environment
- Provide clear, structured responses
- Recommend relevant mobile apps
- Handle chat state in Streamlit
- Keep responses professional and localized to Indian civic services

## Success Criteria
- App starts with `streamlit run app.py`
- All checks pass in CI
- Repository has feature spec files under `specs/janaseva-ai-chatbot/`
