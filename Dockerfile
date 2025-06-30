FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/Tuhinshubhra/CMSeeK.git
WORKDIR /app/CMSeeK
RUN pip install requests flask
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
