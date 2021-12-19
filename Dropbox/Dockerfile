FROM python:3.9

WORKDIR app

COPY cuthbox.py ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "cuthbox.py"]