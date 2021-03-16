import os
from fastapi import APIRouter,Request
from fastapi.responses import FileResponse

images_router = APIRouter(prefix="/image", tags=["images"])

IMAGES_DIR = "images/"

@images_router.get("")
async def get_image(request:Request):
    accept = request.headers.get("accept","image/jpeg")
    format = accept.split("/")[-1].strip()
    if format not in ("jpeg","png","svg","webp"):
        format = "jpeg"
    return FileResponse(path=os.path.join(IMAGES_DIR,f"img.{format}"))


@images_router.get("/jpeg")
async def get_image():
    return FileResponse(path=os.path.join(IMAGES_DIR,"img.jpeg"))


@images_router.get("/png")
async def get_image_png():
    return FileResponse(path=os.path.join(IMAGES_DIR,"img.png"))


@images_router.get("/svg")
async def get_image_svg():
    return FileResponse(path=os.path.join(IMAGES_DIR,"img.svg"))


@images_router.get("/webp")
async def get_image_webp():
    response = FileResponse(path=os.path.join(IMAGES_DIR,"img.webp"))
    response.headers["Content-Type"]="image/webp"
    return response
