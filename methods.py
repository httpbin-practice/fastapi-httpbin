from fastapi import APIRouter, Request
from base import get_base_resp

methods_router = APIRouter(prefix="", tags=["methods"])




@methods_router.get("/get")
async def get(request:Request):
    return get_base_resp(request)


@methods_router.get("/post")
async def post(request:Request):
    return get_base_resp(request)


@methods_router.get("/patch")
async def patch(request:Request):
    return get_base_resp(request)


@methods_router.get("/option")
async def option(request:Request):
    return get_base_resp(request)


@methods_router.get("/delete")
async def delete(request:Request):
    return get_base_resp(request)


@methods_router.get("/head")
async def head():
    return "head"


@methods_router.get("/put")
async def put():
    return "put"
