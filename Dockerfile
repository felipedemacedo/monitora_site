FROM python:3.7

RUN export TZ=America/Noronha

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]