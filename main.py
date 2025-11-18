from gtts import gTTS
import os


input_text = input("Input text: ")


output_filename = "output.mp3"


language = 'en'
myobj = gTTS(text=input_text, lang=language, slow=False)

try:
    myobj.save(output_filename)
    print(f"Audio saved as {output_filename}")
    
    os.startfile(output_filename) 
    
except Exception as e:
    print(f"An error occurred: {e}")