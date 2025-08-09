import streamlit as st

st.title("💻 Coder World 🌍")
st.subheader("🤝 Connect with your coding language")
st.text("🚀 Welcome to your first interactive app")
st.write("🎯 Choose your coding language")


languages = [
    "Python",
    "C",
    "C++",
    "Java",
    "JavaScript",
    "HTML",
    "CSS",
    "PHP",
    "React",
    "SQL"
]

language = st.selectbox("✨ Your favorite coding language:", languages)

st.write(f"✅ You chose **{language}**. Excellent choice! 🎉")
st.success("✅ Your language has been chosen! 🏆")





