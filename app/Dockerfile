FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

EXPOSE 5002

CMD ["shiny", "run", "app.py", "--host", "0.0.0.0", "--port", "5002"]