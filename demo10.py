from gtts import gTTS
import pygame

# Text to be converted to speech
text = "जवान कइला तू सइया राते अबहीं ले दुखात बाटे भरी न सटी दूर तानी हटी धरी न हमके पजा दरदिया उठता ये राजा  कमरिया टूटता ये राजा बात मानी धनिया के बुझी परेशानिया के जनि बानी एतना हेहर जी हम हई राउर मेहर जी जाइ बहरा अब देर ना लगाई बजी न हाउ अब बजा दरदिया उठता ये राजा कमरिया टूटता ये राजा दरदिया उठता ये राजा सुना प्रमोद पिया हो धड़के ला जिया हो  "

# Create a gTTS object
tts = gTTS(text)

# Save the speech as an audio file (optional)
tts.save("output.mp3")

# Initialize the mixer module
pygame.mixer.init()

# Load the saved MP3 file
pygame.mixer.music.load("output.mp3")

# Play the speech
pygame.mixer.music.play()

# Wait for the speech to finish playing
pygame.time.wait(5000)  # You can adjust the time in milliseconds (5000 = 5 seconds)

# Clean up the mixer
pygame.mixer.quit()
