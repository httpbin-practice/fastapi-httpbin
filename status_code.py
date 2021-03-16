from fastapi import APIRouter

status_router = APIRouter(prefix="/status", tags=["status"])


@status_router.get("/{codes}")
async def get_status(codes):
    return codes


@status_router.delete("/{codes}")
async def delete_status(codes):
    return codes


@status_router.put("/{codes}")
async def put_status(codes):
    return codes


@status_router.post("/{codes}")
async def post_status(codes):
    return codes


@status_router.patch("/{codes}")
async def patch_status(codes):
    return codes
