from fastapi import APIRouter

cookies_router = APIRouter(prefix="/cookies", tags=["cookies"])


@cookies_router.get("")
async def get_cookies():
    return "get cookies"


@cookies_router.get("/delete")
async def get_cookies_delete():
    return "get cookies delete"


@cookies_router.get("/set")
async def get_cookies_set():
    return "get cookies set"


@cookies_router.get("/set/{name}/key")
async def get_cookies_set_name_key(name, key):
    return {name: key}
