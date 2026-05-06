FROM python:3.10-slim

WORKDIR /app

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 9000

CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
