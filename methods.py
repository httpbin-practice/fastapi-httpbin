from fastapi import APIRouter

methods_router = APIRouter(prefix="", tags=["methods"])


@methods_router.get("/get")
async def get():
    return "get"


@methods_router.get("/post")
async def post():
    return "post"


@methods_router.get("/patch")
async def patch():
    return "patch"


@methods_router.get("/option")
async def option():
    return "option"


@methods_router.get("/delete")
async def delete():
    return "delete"


@methods_router.get("/head")
async def head():
    return "head"


@methods_router.get("/put")
async def put():
    return "put"
