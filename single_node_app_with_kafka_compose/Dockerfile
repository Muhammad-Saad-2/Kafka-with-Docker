FROM python:3.12
 
RUN pip install poetry

WORKDIR /code

# Copy the pyproject.toml file to the container
ADD ./pyproject.toml /code/

# Copy the rest of the application code to the container
ADD . /code/

RUN poetry config virtualenvs.create false 

RUN poetry install

CMD ["poetry", "run", "uvicorn", "app.main:app", "host",  "0.0.0.0", "--reload" ]



