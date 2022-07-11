FROM python:3.10.4

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN bash setup.sh

EXPOSE 8000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0"]