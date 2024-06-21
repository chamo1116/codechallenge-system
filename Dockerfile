FROM python:3.10 as python-base

RUN pip install poetry

COPY . .

RUN poetry install

# Run Application
CMD [ "poetry", "run", "python", "-m", "ingest_system.main"]