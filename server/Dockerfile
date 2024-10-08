FROM python:3.12

WORKDIR /
COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 4000

CMD [ "uvicorn", "server/src/server:app", "--reload" ]