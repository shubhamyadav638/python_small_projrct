from gtts import gTTS
import os

# Hindi text you want to convert to speech
hindi_text = "नमस्ते, यह एक उदाहरण है कि कैसे हम Python में टेक्स्ट को ऑडियो में बदल सकते हैं।"

# Create a gTTS object
tts = gTTS(text=hindi_text, lang='hi')

# Save the generated speech to a file (optional)
tts.save("output.mp3")

# Play the generated speech (optional)
os.system("mpg321 output.mp3")  # You can use any suitable audio player here

# Alternatively, you can also directly play the speech without saving it to a file
# tts.save("output.mp3")
# tts.play()
