# web app of weather and a simple chatbbot by using streamlit framework

import streamlit as st
from google import genai
import requests

def chatbot():
    API_KEY = "AQ.Ab8RN6J-a_v3yqL_yHV9rOtdynuZJosserUbqnN29G2n_mqX9A"

    client = genai.Client(api_key=API_KEY)

    # Streamlit Page

    st.title(" AI Chatbot")
    st.write("Ask me anything!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Input

    prompt = st.chat_input("Type your message...")

    if prompt:

        # Display user message
        st.chat_message("user").markdown(prompt)

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        try:
            # Generate AI Response
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            answer = response.text

        except Exception as e:
            answer = f"Error: {e}"

        # Display assistant response
        st.chat_message("assistant").markdown(answer)

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

#function for weather app
def weather_app():
    # OpenWeather API Key
    API_KEY   = "879786c25bef84366a1502e0947dd186"

# Page Configuration


    st.title(" Weather App")
    st.write("Check current weather using OpenWeather API")

    # Input City
    city = st.text_input("Enter City Name")

    if st.button("search weather"):

        if city == "":
            st.warning("Please enter a city name.")
        else:

            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

            response = requests.get(url)

            data = response.json()

            if response.status_code == 200:

                temperature = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                humidity = data["main"]["humidity"]
                pressure = data["main"]["pressure"]

                weather = data["weather"][0]["main"]
                description = data["weather"][0]["description"]

                wind_speed = data["wind"]["speed"]

                st.success("Weather Found Successfully!")

                st.subheader(f" {city.title()}")

                st.metric(" Temperature", f"{temperature} °C")
                st.metric("Feels Like", f"{feels_like} °C")

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f" Humidity: **{humidity}%**")
                    st.write(f" Wind Speed: **{wind_speed} m/s**")

                with col2:
                    st.write(f" Pressure: **{pressure} hPa**")
                    st.write(f" Weather: **{weather}**")

                st.info(description.title())

            else:
                st.error("City not found!")

st.set_page_config(
    page_title="Weather and Chatbot App",
    layout="wide"
)
page = st.sidebar.selectbox(
    "Select a page",
    ["Home", "Chatbot", "Weather App"]
)

if page == "Weather and Chatbot App":
    st.title("Welcome to Weather and Chatbot App")
    st.write("This app allows you to check the weather and chat with an AI chatbot.")
    st.write("Use the sidebar to navigate between the Chatbot and Weather App pages.")
elif page == "Home":
    st.header("home page")
    st.title("Welcome to Weather and Chatbot App")
    st.write("This app allows you to check the weather and chat with an AI chatbot.")
    st.write("Use the sidebar to navigate between the Chatbot and Weather App pages.")
elif page == "Chatbot":
    chatbot()
elif page == "Weather App":
    weather_app()
else:
    st.warning("thank you for using this app.")