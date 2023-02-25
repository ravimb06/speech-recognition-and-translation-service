FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    ffmpeg \
    fontconfig \
    libfontconfig1 \
    libfreetype6 \
    libx11-6 \
    libxext6 \
    libxrender1 \
    xfonts-75dpi \
    xfonts-base \
&& rm -rf /var/lib/apt/lists/*

COPY arial.ttf /usr/share/fonts/truetype/
COPY ./requirements.txt requirements.txt
COPY ./.env .env


RUN fc-cache -f -v
RUN pip install -r requirements.txt

COPY src .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
