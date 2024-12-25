# setup
#
# !pip install tiktoken==0.7.0
# !pip install openai==1.40.6 httpx==0.27.2
#
#

"""
requires:

(env)
OpenAI モジュールは環境変数を見に行くので以下の変数を別途設定して下さい。

OPENAI_API_KEY

"""



import tiktoken
from openai import OpenAI


def C2Sample_printTiktokens1():
	text = "ChatGPT"
	encoding = tiktoken.encoding_for_model("gpt-4o")
	tokens = encoding.encode(text)
	for token in tokens:
		print(encoding.decode([token]))


def C2Sample_printTiktokens2():
	text = "LLMを使ってクールなものを作るのは簡単だが、プロダクションで使えるものを作るのは非常に難しい。"
	encoding = tiktoken.encoding_for_model("gpt-4o")
	tokens = encoding.encode(text)
	print(len(tokens))


def C2Sample_openai01():
	print( "Chat Completions API の呼び出し")
	client = OpenAI()
	response = client.chat.completions.create(
		model="gpt-4o-mini",
		messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{"role": "user", "content": "こんにちは！私はジョンと言います！"},
		],
	)
	print(response.to_json(indent=2))


def C2Sample_openai02():
	print("会話履歴を踏まえた応答を得る")

	client = OpenAI()
	response = client.chat.completions.create(
		model="gpt-4o-mini",
		messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{"role": "user", "content": "こんにちは！私はジョンと言います！"},
			{"role": "assistant", "content": "こんにちは、ジョンさん！お会いできて嬉しいです。今日はどんなことをお話ししましょうか？"},
			{"role": "user", "content": "私の名前が分かりますか？"},
		],
	)
	print(response.to_json(indent=2))


def C2Sample_openai03():
	print("ストリーミングで応答を得る")
	client = OpenAI()
	response = client.chat.completions.create(
	    model="gpt-4o-mini",
	    messages=[
	        {"role": "system", "content": "You are a helpful assistant."},
	        {"role": "user", "content": "こんにちは！私はジョンと言います！"},
	    ],
	    stream=True,
	)
	
	for chunk in response:
	    content = chunk.choices[0].delta.content
	    if content is not None:
	        print(content, end="", flush=True)
	

def C2Sample_openai04():
	client = OpenAI()
	response = client.chat.completions.create(
	    model="gpt-4o-mini",
	    messages=[
	        {
	            "role": "system",
	            "content": '人物一覧を次のJSON形式で出力してください。\n{"people": ["aaa", "bbb"]}',
	        },
	        {
	            "role": "user",
	            "content": "昔々あるところにおじいさんとおばあさんがいました",
	        },
	    ],
	    response_format={"type": "json_object"},
	)
	print(response.choices[0].message.content)	
	

def C2Sample_openai05():
	print("Vision（画像入力）")
	client = OpenAI()
	image_url = "https://raw.githubusercontent.com/yoshidashingo/langchain-book/main/assets/cover.jpg"
	response = client.chat.completions.create(
	    model="gpt-4o-mini",
	    messages=[
	        {
	            "role": "user",
	            "content": [
	                {"type": "text", "text": "画像を説明してください。"},
	                {"type": "image_url", "image_url": {"url": image_url}},
	            ],
	        }
	    ],
	)
	print(response.choices[0].message.content)
	


def C2Sample_openai05():
	print("Completions API")
	client = OpenAI()
	response = client.completions.create(
	    model="gpt-3.5-turbo-instruct",
	    prompt="こんにちは！私はジョンと言います！",
	)
	
	
	
	
	
	
	
