FROM python:3.14

WORKDIR /app

COPY . .

CMD ["sh", "-c", "python main.py && tail -f /dev/null"]