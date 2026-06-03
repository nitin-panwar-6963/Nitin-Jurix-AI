FROM python:3.9-slim

# CREATE A DIRECTORY WHERE WE STORE THE CODE
WORKDIR /app

# download big thing
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        tesseract-ocr \
        gcc \
        python3-dev && \
    rm -rf /var/lib/apt/lists/*

#to remove the vulerabilites
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# download the langchain
RUN pip install -U langchain-chroma

# COPY ALL REQUIREMEMT TO THAT
COPY requirements.txt .

# UPDATE PIP
RUN pip install --upgrade pip


#torch download
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# INSTALL ALL DEPENDENCY
RUN pip install --default-timeout=1000  --no-cache-dir -r requirements.txt \
    && pip install gunicorn

# COPY ALL CODE FROM LOCAL TO HOST
COPY . .

# ACCESS PORT NUMBER
EXPOSE 8000

# RUN THE APP ON GUNICORN SERVER
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "backend:app"]
