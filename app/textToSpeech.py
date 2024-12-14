from pathlib import Path
from openai import OpenAI
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

client = OpenAI(api_key="")

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="onyx",
  input="Hello, how are you today my friend?"
)

response.stream_to_file(speech_file_path)