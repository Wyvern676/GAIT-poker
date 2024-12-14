from openai import OpenAI

client = OpenAI(api_key="")

response = client.images.generate(
    prompt="a broccoli tree",
    n=2,
    size="1024x1024"
)

print(response.data[0].url)