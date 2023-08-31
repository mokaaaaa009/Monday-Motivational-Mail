import os
import requests
import PyPDF2
import pyttsx3

CHUNK_SIZE = 100
ENDPOINT = "https://api.elevenlabs.io/v1/text-to-speech/AZnzlk1XvdvUeBnXmlld"
API_KEY = os.environ.get("API_KEY")

# TO DO : find a way to load pdf file
with open(r"stories/Short-stories-Sherwood-Anderson-The-Dumb-Man.pdf", 'rb') as pdfObj:
    pdfReader = PyPDF2.PdfReader(pdfObj)
    pages = pdfReader.pages
    content = pages[0].extract_text()


#using pyttsx3
# engine = pyttsx3.init()
# engine.say(content)
# engine.save_to_file("TheDumbMan","Dumbman.mp3")
# engine.runAndWait()


#
# # TO DO:send file to API to transform to AUDIO
headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": API_KEY
}
data = {
    "text":content,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
}

response = requests.post(ENDPOINT, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)







# TO DO:Create web page accept pdf file and show audio file to the user
