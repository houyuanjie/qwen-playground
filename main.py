from transformers import pipeline

model = "Qwen/Qwen2.5-0.5B-Instruct"
pipe = pipeline("text-generation", model, torch_dtype="auto", device_map="auto")
messages = []


def chat(prompt, max_new_tokens=512):
    message = {"role": "user", "content": prompt}
    print(message)
    messages.append(message)
    response_message = pipe(messages, max_new_tokens=max_new_tokens)[0]["generated_text"][-1]
    print(response_message)
    messages.append(response_message)


chat("你好。")
chat("你是谁？")
chat("单词Strawberry中有几个字母r？")
