FROM python:3.9-slim-buster as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source and tests
COPY my_app/ my_app/
COPY tests/ tests/

# Run tests
RUN pytest --maxfail=1 --disable-warnings -q

# If tests pass, build final image
FROM python:3.9-slim-buster
WORKDIR /app
COPY --from=builder /app/my_app/ my_app/
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "my_app/main.py", "$OPERATION", "$NUM1", "$NUM2"]