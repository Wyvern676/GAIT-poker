import openai

# Set your OpenAI API key
openai.api_key = "your_api_key_here"

# Create a chat completion with streaming
stream = openai.ChatCompletion.create(
    model="gpt-4-turbo",  
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)

# Print the streamed content
for chunk in stream:
    # Check if the chunk contains content and print it
    if "choices" in chunk and chunk["choices"][0]["delta"].get("content"):
        print(chunk["choices"][0]["delta"]["content"], end="")
