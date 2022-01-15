FROM ubuntu:18.04
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    python3 \
    #python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove

RUN apt-get update -qq && apt-get install -y build-essential libsqlite3-dev \
  libpng-dev libjpeg-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install pytesseract

COPY . .
EXPOSE 5000

CMD ["python3", "app.py"]