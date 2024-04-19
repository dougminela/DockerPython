FROM python:3.11

COPY . /Main/exerciciospy

WORKDIR /Main/exerciciospy

CMD ["python", "main.py"]