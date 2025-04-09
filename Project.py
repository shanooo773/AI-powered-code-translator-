from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "Salesforce/codegen-2B-multi" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype=torch.float16)

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


if __name__ == "__main__":
    python_code = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
"""

    target_lang = "C++"
    print(f"🔄 Converting to {target_lang}...\n")
    converted = convert_code(python_code, target_language=target_lang)
    print("✅ Converted Code:\n")
    print(converted)
