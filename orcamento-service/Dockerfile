# Dockerfile
FROM python:3.7
COPY requirements.txt /orcamentoapp/requirements.txt
WORKDIR /orcamentoapp
RUN pip install -r requirements.txt
COPY . /orcamentoapp
ENTRYPOINT ["python"]
CMD ["run.py"]