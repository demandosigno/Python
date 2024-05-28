from openai import OpenAI

# client = OpenAI()

# もし環境変数が使えないなら次のようにする：
# 削除

res = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "あなたは賢いAIです。"},  # 役割設定（省略可）
        {"role": "user", "content": "1たす1は？"}               # 最初の質問
    ],
    temperature=1  # 温度（0-2, デフォルト1）
)

print(res.choices[0].message.content)  # 答えが返る