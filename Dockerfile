FROM python:3.9-buster
WORKDIR /chatbot
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]