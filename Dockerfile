FROM ghcr.io/astral-sh/uv:latest AS uv
FROM python:3.11-slim

WORKDIR /app
COPY --from=uv /uv /bin/uv

# Install dependencies during build so the cloud doesn't have to
COPY pyproject.toml .
RUN uv sync --frozen

COPY . .

# Digital Ocean uses the PORT environment variable
# We bind to 0.0.0.0 and use the $PORT variable provided by DO
CMD ["sh", "-c", "uv run gunicorn --bind 0.0.0.0:${PORT:-5000} run:app --workers 4"]