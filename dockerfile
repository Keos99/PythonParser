FROM python:3

VOLUME /app/news
WORKDIR /app/src

RUN python3 -m venv env
ADD database.py main.py urlparser.py requirements.txt ./
CMD ['source', 'env/bin/activate']
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "./main.py" ]
