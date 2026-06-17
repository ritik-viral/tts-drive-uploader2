from flask import Flask, request
from gtts import gTTS
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

app = Flask(__name__)

FOLDER_ID = "1RPWcXCCUSAfRv0CPJE5tnOp_MZPuYbeN"

SCOPES = ['https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file(
'credentials.json',
scopes=SCOPES
)

drive_service = build('drive', 'v3', credentials=credentials)

@app.route("/", methods=["GET"])
def home():
    return "Working"

@app.route("/generate", methods=["POST"])
def generate():

text = request.form.get("text") if not text: return "No text provided" tts = gTTS(text=text, lang="hi") filename = "final.wav" tts.save(filename) file_metadata = { 'name': filename, 'parents': [FOLDER_ID] } media = MediaFileUpload(filename) uploaded = drive_service.files().create( body=file_metadata, media_body=media, fields='id' ).execute() return f"Uploaded File ID: {uploaded['id']}" 

if __name__ == "__main__":
app.run(host="0.0.0.0", port=10000)

