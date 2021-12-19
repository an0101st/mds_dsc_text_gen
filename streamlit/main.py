import streamlit as st
from transformers import pipeline, set_seed

st.title("Text Generator")
st.write("Type a text and let the model generate further sentences")
text = st.text_input("Insert a text")

if st.button("Generate further Text") \
    and text is not None:
        generator = pipeline('text-generation', model='gpt2')
        set_seed(42)
        output = generator(text, max_length=10, num_return_sequences=5)
        st.write(output)
