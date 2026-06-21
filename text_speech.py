import gtts
import playsound3
text = input("Enter a sentence here: ")
sound = gtts.gTTS(text, lang="en")
sound.save("Welcome.mp3")
playsound3.playsound("Welcome.mp3")
