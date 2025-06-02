FROM python:3.9-slim 

WORKDIR /api

# Copy requirements.txt in so that pip can access it
COPY requirements.txt requirements.txt

# Install the requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python","api.py"]
