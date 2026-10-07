FROM python:3.12-slim AS builder

WORKDIR /build

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
PATH="/opt/venv/bin:$PATH" 

WORKDIR /app

# Copy dependency files from build to runtime
COPY --from=builder /opt/venv /opt/venv

# create a non-root user
RUN useradd --create-home --uid 1002 order-user

# copy, grant ownership, and permission to the non-root user to the application directory
COPY --chown=order-user:order-user main.py .

# set appuser
USER order-user

# expose port
EXPOSE 8000

# perform health check on container
HEALTHCHECK \
--interval=30s \
--timeout=30s \
--start-period=5s \
--retries=3 \
CMD python -c "import urllib.request; urllib.request.urlopen('http://0.0.0.0:8001/health', timeout=30)"

# run final application commnands
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]