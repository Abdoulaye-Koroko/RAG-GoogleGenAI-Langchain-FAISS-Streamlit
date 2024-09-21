FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN pip install poetry

RUN poetry install --no-root

COPY .env /app/

COPY app /app/

WORKDIR /app/app

# Expose the port that Streamlit uses
EXPOSE 8501

# Set the entry point for the container
CMD ["poetry", "run", "streamlit", "run", "app.py"]
