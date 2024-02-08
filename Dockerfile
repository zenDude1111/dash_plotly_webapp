FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:2718", "app:server"]

