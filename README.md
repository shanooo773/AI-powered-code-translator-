Perfect! Here's the updated `README.md` with **all required pip installs**, including support packages like `sentencepiece` (some transformer models need this) and `accelerate` (helps with faster GPU/CPU switching):

---

```markdown
# 🤖 AI Code Converter

Convert Python code into other popular programming languages like C++, Java, JavaScript, and more — using an AI model powered by **Salesforce CodeGen** and **Hugging Face Transformers**.  
This project has a clean Streamlit UI and uses deep learning to help developers translate code without memorizing syntax.

---

## 🌟 Features

- 🔄 Convert Python code into:
  - C++
  - Java
  - JavaScript
  - C#
  - Go
  - Rust
- 💡 Built with `transformers`, `torch`, and `streamlit`
- ⚡ Fast inference using GPU (if available)
- 🎛️ Streamlit UI for easy interaction

---

## 🚀 Demo

![demo](screenshot.png)

---

## 🔧 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/ai-code-converter.git
cd ai-code-converter
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate    # on Windows
source venv/bin/activate # on Linux/Mac
```

### 3. Install dependencies

Run the following to install all required libraries:
```bash
pip install torch transformers streamlit sentencepiece accelerate
```

> If you're using Python 3.12 and face any issues with `torch`, you can install it using the official instructions: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

### 4. Run the app
```bash
streamlit run code_converter_gui.py
```

---

## 📦 Requirements

- Python 3.9 or higher
- `torch`
- `transformers`
- `streamlit`
- `sentencepiece`
- `accelerate`

---

## 💡 Example Prompt

Input (Python):
```python
def add(a, b):
    return a + b
```

Converted Output (C++):
```cpp
int add(int a, int b) {
    return a + b;
}
```

---

## 📌 Notes

- Model used: `Salesforce/codegen-2B-multi`
- Internet connection is required on first run to download the model from Hugging Face
- Performance improves with a GPU (but works on CPU too)



---

## 👨‍💻 Author

**Shayan Humayun**  
Computer Engineering Student at UET Taxila  

---

```

Let me know if you'd like the `requirements.txt` file generated from that list too. I can also help write a `.gitignore`, `LICENSE`, or add GitHub badges if you want to make it even cooler 💻🔥
