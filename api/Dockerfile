FROM python:3.14-alpine
WORKDIR /api
RUN pip install poetry pip --upgrade
COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction
COPY . .
RUN chmod +x ./start.sh
RUN chmod +x ./prestart.sh
ENTRYPOINT [ "sh", "./prestart.sh" ]
CMD [ "sh", "./start.sh" ]