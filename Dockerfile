FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=source

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--access-logfile=-", "source:create_app()"]