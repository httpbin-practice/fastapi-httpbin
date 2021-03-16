from fastapi import APIRouter

response_format_router = APIRouter(prefix="/response-format", tags=["response formats"])


@response_format_router.get("/brotli")
async def get_response_format_brotli():
    return "get_response_format_brotli"


@response_format_router.get("/deflate")
async def get_response_format_deflate():
    return "get_response_format_deflate"


@response_format_router.get("/deny")
async def get_response_format_deny():
    return "get_response_format_deny"


@response_format_router.get("/ecoding/utf8")
async def get_response_format_ecoding_utf8():
    return "get_response_format_ecoding_utf8"


@response_format_router.get("/gzip")
async def get_response_format_gzip():
    return "get_response_format_gzip"


@response_format_router.get("/html")
async def get_response_format_html():
    return "get_response_format_html"


@response_format_router.get("/json")
async def get_response_format_json():
    return "get_response_format_json"


@response_format_router.get("/robots.txt")
async def get_response_format_robots_txt():
    return "get_response_format_robots_txt"


@response_format_router.get("/xml")
async def get_response_format_xml():
    return "get_response_format_xml"
