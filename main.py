from fastapi import FastAPI,Request
from fastapi.middleware.gzip import GZipMiddleware
from status_code import status_router
from methods import methods_router
from anything import anything_router
from images import images_router
from cookies import cookies_router
from redirects import redirects_router
from auth import auth_router
from response_formats import response_format_router
from request_inspection import request_insepct_router
from response_inspection import response_inspect_router
from dynamic_data import dynamic_data_router

app = FastAPI(
    title="FastAPI-httpbin",
    description="A simple HTTP Request & Response Service.",
    version="0.1.0",
)

app.add_middleware(GZipMiddleware, minimum_size=0)


app.include_router(methods_router)
app.include_router(status_router)
app.include_router(images_router)
app.include_router(request_insepct_router)
app.include_router(response_inspect_router)
app.include_router(response_format_router)
app.include_router(redirects_router)
app.include_router(cookies_router)
app.include_router(dynamic_data_router)
app.include_router(auth_router)
app.include_router(anything_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",headers=[("server","FastAPI-HTTPBIN")], host="0.0.0.0", port=8000, reload=True)
