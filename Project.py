# code_converter_gui.py

import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and tokenizer (once at start)
@st.cache_resource
def load_model():
    model_name = "Salesforce/codegen-2B-multi"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16
    )
    return tokenizer, model

tokenizer, model = load_model()

# Convert code function
def convert_code(input_code, target_language="C++"):
    prompt = f"""##### Convert the following Python code to {target_language}:\n### Python\n{input_code}\n### {target_language}\n"""
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_length=512,
        temperature=0.3,
        top_p=0.95,
        do_sample=True,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    translated_code = result.split(f"### {target_language}")[-1].strip()
    return translated_code

# Streamlit UI
st.set_page_config(page_title="AI Code Converter", layout="wide")
st.title("🤖 AI Code Converter")
st.write("Paste your Python code below and choose a language to convert it into.")

# Text input
input_code = st.text_area("📝 Python Code", height=250)

# Language selector
language = st.selectbox("🌐 Convert to language", ["C++", "Java", "JavaScript", "C#", "Go", "Rust"])

# Convert button
if st.button("🔁 Convert"):
    if input_code.strip() == "":
        st.warning("Please enter some Python code first!")
    else:
        with st.spinner("Converting..."):
            result = convert_code(input_code, target_language=language)
            st.success("✅ Code Converted Successfully!")

            st.code(result, language.lower())
