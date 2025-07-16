# ──────────────────────────────────────────────────────────────
# backend/Dockerfile  →  builds the FastAPI application image
# ──────────────────────────────────────────────────────────────

# 1️⃣  Base image ─ choose an official Python runtime
FROM python:3.10-slim

# 2️⃣  Set work directory inside the container
WORKDIR /app

# 3️⃣  Copy application files *into* the image
#     Using two COPY commands keeps rebuilds faster:
#     - first copy only requirements.txt so deps are cached
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#     - then copy the rest of the backend code
COPY . .

# 4️⃣  Expose the port where Uvicorn will run
EXPOSE 8000

# 5️⃣  Default command: launch FastAPI with auto‑reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
