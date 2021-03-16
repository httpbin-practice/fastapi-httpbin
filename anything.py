from fastapi import APIRouter

anything_router = APIRouter(
    prefix="/anything", tags=["anything"]
)


@anything_router.delete("")
async def delete_anything():
    return "delete_anything"


@anything_router.patch("")
async def patch_anything():
    return "patch_anything"


@anything_router.get("")
async def get_anything():
    return "get_anything"


@anything_router.post("")
async def post_anything():
    return "post_anything"


@anything_router.put("")
async def put_anything():
    return "put_anything"


@anything_router.delete("/{anything}")
async def delete_anything_i(anything):
    return anything


@anything_router.patch("/anything")
async def patch_anything_i(anything):
    return anything


@anything_router.get("/{anything}")
async def get_anything_i(anything):
    return anything


@anything_router.post("/{anything}")
async def post_anything_i(anything):
    return anything


@anything_router.put("/{anything}")
async def put_anything_i(anything):
    return anything
