import openai

openai.api_key = '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'

#engines = openai.Engine.list()
#print(engines.data)

"""
# Tạo 1 prompt để gửi đến api
prompt = "Viết một đoạn văn về chủ đề 'Việt Nam'"

# Gọi api và lấy kết quả
response = openai.Completion.create(
    engine="model_id",#"text-davinci-002",
    prompt=prompt,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.5,
)

# Hiển thị câu trả lời
print(response["choices"][0]["text"])
"""
# choose text to embed
text_string = "sample text"

# choose an embedding
model_id = "text-similarity-davinci-001"

# compute the embedding of the text
embedding = openai.Embedding.create(input=text_string, engine=model_id)['data'][0]['embedding']
print(embedding)