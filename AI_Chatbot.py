import groq
import streamlit as st
import openai

openai.api_key = "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"

def get_user_input():
    user_input = st.text_input("Enter your message:")
    return user_input.strip() if user_input else None

def generate_response(user_input):
    if not user_input:
        return "Please enter a message."

    # Define your OpenAI prompt and temperature settings
    prompt = f"You: {user_input}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Adjust engine as needed
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7  # Adjust temperature for response creativity
    )
    return response.choices[0].text.strip()

st.title("My AI Chatbot")

user_message = get_user_input()

if user_message:
    response = generate_response(user_message)
    st.write(f"AI: {response}")
