FROM python:3.10.11-bullseye

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /src/ /app/
COPY search-result.json search-result.json
RUN ls /app/

CMD ["python", "main.py"]