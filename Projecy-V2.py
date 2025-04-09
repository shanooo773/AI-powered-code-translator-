# Install required packages
!pip install streamlit transformers torch sentencepiece accelerate pyngrok

# Write your Streamlit app to a file
code = '''
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import logging
logging.getLogger("streamlit.runtime.scriptrunner.script_run_context").setLevel(logging.ERROR)

import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

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

st.set_page_config(page_title="AI Code Converter", layout="wide")
st.title("🤖 AI Code Converter")
st.write("Paste your Python code below and choose a language to convert it into.")

input_code = st.text_area("📝 Python Code", height=250)
language = st.selectbox("🌐 Convert to language", ["C++", "Java", "JavaScript", "C#", "Go", "Rust"])

if st.button("🔁 Convert"):
    if input_code.strip() == "":
        st.warning("Please enter some Python code first!")
    else:
        with st.spinner("Converting..."):
            result = convert_code(input_code, target_language=language)
            st.success("✅ Code Converted Successfully!")
            st.code(result, language.lower())
'''

with open("code_converter_gui.py", "w") as f:
    f.write(code)

# Start Streamlit app in background and expose via ngrok
from pyngrok import ngrok
import threading
import time

# ✅ Set your authtoken here (REQUIRED)
ngrok.set_auth_token("2vTIb7nPIwdKSLmuiklFgw6PKFJ_5i4ALMgB8A3zh8eUYHd4v")

def run():
    !streamlit run code_converter_gui.py &

threading.Thread(target=run).start()
time.sleep(5)

# Create and print public URL
public_url = ngrok.connect("http://localhost:8501")

print("🔗 Streamlit app is live at:", public_url)
