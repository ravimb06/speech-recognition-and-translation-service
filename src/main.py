import os
import asyncio

from fastapi import FastAPI, Request, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv

import whisper
import ffmpeg
import deepl
import numpy as np

from pdf.to_pdf import save_to_pdf

load_dotenv()

DEEPL_AUTH_KEY = os.getenv("DEEPL_KEY")


def getAudioBuffer(file, start, length):

    out, _ = (
                ffmpeg.input(file, threads=0)
                .output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=16000, ss=start, t=length)
                .run(cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True)
            )

    return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0


app = FastAPI()


app.mount('/static', StaticFiles(directory='static'), name='static')
template = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return template.TemplateResponse('index.html',  {"request": request, "text": None})


@app.post('/')
def add_audio(request: Request, file: bytes = File()):
    with open('audio.mp3', 'wb') as f:
        f.write(file)
    
    data = request.form()
    super_data = asyncio.run(data)
    model_type = super_data['model_type']
    model = whisper.load_model(model_type)
    translator = deepl.Translator(DEEPL_AUTH_KEY)
    result = model.transcribe("audio.mp3", fp16=False)
    translated_text = translator.translate_text(result['text'], target_lang=super_data['language'])
    save_to_pdf(translated_text.text, 'translated_text.pdf')
    return template.TemplateResponse('index.html',  {
        "request": request, "text": translated_text.text
        }
    )


@app.get("/download_file")
async def download_file():
    file_path = os.path.abspath('translated_text.pdf')
    return FileResponse(file_path, media_type="application/pdf")
