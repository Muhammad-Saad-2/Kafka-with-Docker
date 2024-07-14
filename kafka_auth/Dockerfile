FROM python:3.12
 
RUN pip install poetry

WORKDIR /code

ADD ./pyproject.toml /code/

ADD ./app /code/app 

RUN poetry config virtualenvs.create false 

RUN poetry install

CMD ["poetry", "run", "uvicorn", "app.main:app", "host",  "0.0.0.0", "--reload" ]



