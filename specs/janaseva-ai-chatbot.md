# JanSeva AI Chatbot Specification

## Purpose
Create an AI civic assistant for Indian citizens.

## Features

### AI Chat
- User can ask civic questions
- AI answers using Groq API
- Chat history maintained

### Services Supported
- Aadhaar services
- Government schemes
- Road complaints
- Garbage complaints
- Electricity complaints

### App Recommendation
Each response should contain:
- App Name
- Platform
- Official Link
- Description

## Technology
- Python
- Streamlit
- Groq API
- SQLite

## Security
- API key stored in environment variables
- No secrets in code

## Testing
- Test chatbot response
- Test UI
- Test deployment