from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Sample API",
        version="1.0.0",
        description="Sample API",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

instrumentator = Instrumentator().instrument(app)
instrumentator.expose(app, include_in_schema=False)

@app.get("/api/v1/health", description="API status check", tags=["Common"])
def check_health():
    return {
        "status": "OK"
    }
