import openai

# OpenAI APIキーの設定
# 削除

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # 使用するモデルを指定（例: text-davinci-003）
        prompt=prompt,
        max_tokens=150,  # 応答の最大トークン数
        n=1,  # 応答の数
        stop=None,  # 応答を停止させるトークン（省略可能）
        temperature=0.7  # 応答の多様性を決定するパラメータ（0.0-1.0）
    )
    return response.choices[0].text.strip()

# 使用例
user_input = "ChatGPTでAPIを利用する方法を教えてください。"
response = chat_with_gpt(user_input)
print("ChatGPTの応答:", response)
