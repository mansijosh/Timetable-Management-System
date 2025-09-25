import time
import logging
from fastapi import FastAPI, Request

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def add_timing_middleware(app: FastAPI):
    @app.middleware("http")
    async def log_request_time(request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        duration = time.perf_counter() - start

        logger.info(
            "method=%s path=%s status=%s duration=%.4fs",
            request.method,
            request.url.path,
            response.status_code,
            duration
        )

        response.headers["X-Process-Time"] = f"{duration:.4f}s"
        return response
