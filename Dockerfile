FROM python:3.12-slim
WORKDIR /code
COPY --from=ghcr.io/astral-sh/uv:0.12.0 /uv /bin/uv
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-cache
COPY app ./app
EXPOSE 8000
CMD ["/code/.venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
