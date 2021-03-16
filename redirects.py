from fastapi import APIRouter

redirects_router = APIRouter(prefix="/redirect", tags=["redirects"])


@redirects_router.get("/absolute-redirect/{n}")
async def get_absolute_redirect_n(n):
    return "get_absolute_redirect_n"


@redirects_router.delete("/redirect-to")
async def delete_redirect_to():
    return "delete_redirect_to"


@redirects_router.get("/redirect-to")
async def get_redirect_to():
    return "get_redirect_to"


@redirects_router.patch("/redirect-to")
async def patch_redirect_to():
    return "patch_redirect_to"


@redirects_router.post("/redirect-to")
async def post_redirect_to():
    return "post_redirect_to"


@redirects_router.put("/redirect-to")
async def put_redirect_to():
    return "put_redirect_to"


@redirects_router.get("/redirect/{n}")
async def get_redirect_n(n):
    return "get_redirect_n"


@redirects_router.get("/relative-redirect/{n}")
async def get_relative_redirect_n(n):
    return "get_relative_redirect_n"
