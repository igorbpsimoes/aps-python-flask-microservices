# Dockerfile
FROM python:3.7
COPY requirements.txt /gastoapp/requirements.txt
WORKDIR /gastoapp
RUN pip install -r requirements.txt
COPY . /gastoapp
ENTRYPOINT ["python"]
CMD ["run.py"]
