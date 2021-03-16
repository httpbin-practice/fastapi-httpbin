from fastapi import APIRouter

images_router = APIRouter(prefix="/image", tags=["images"])


@images_router.get("")
async def get_image():
    return "get image"


@images_router.get("/jpeg")
async def get_image():
    return "get image jpeg"


@images_router.get("/png")
async def get_image_png():
    return "get image png"


@images_router.get("/svg")
async def get_image_svg():
    return "get image svg"


@images_router.get("/webp")
async def get_image_webp():
    return "get image webp"
