FROM python:3.14.2-alpine
WORKDIR /api
RUN pip install pip poetry --upgrade
COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock
RUN poetry config virtualenvs.create false
RUN poetry install -n
COPY . .
RUN chmod +x ./prestart.sh
ENTRYPOINT [ "sh", "./prestart.sh" ]
CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]