import streamlit as st
from rephraser import rephrase_with_tone
from tone_classifier import tone_score

st.title("🧠 REPHRASINATOR - Intelligent Text Rephraser")
st.write("Rephrase your text in different tones using NLP Transformer models.")

text = st.text_area("✍️ Enter your text here:")
tone = st.selectbox("🎨 Choose tone:", ["formal", "informal", "concise", "friendly", "creative"])
temperature = st.slider("🔥 Creativity (temperature):", 0.1, 1.0, 0.7)
num_beams = st.slider("🧭 Precision (num_beams):", 1, 10, 5)

if st.button("Rephrase"):
    if text.strip():
        result = rephrase_with_tone(text, tone=tone, temperature=temperature, num_beams=num_beams)
        st.subheader("💬 Rephrased Output:")
        st.write(result)
        
        # Tone score
        score = tone_score(result, tone)
        st.progress(score)
        st.caption(f"Tone match score: {score:.2f}")
    else:
        st.warning("Please enter some text to rephrase.")
