from fastapi import APIRouter,Response

response_inspect_router = APIRouter(prefix="/response_inspect", tags=["response inspection"])

CACHE = {}

@response_inspect_router.get("/cache")
async def get_response_cache():
    return "get_response_cache"


@response_inspect_router.get("/cache/{value}")
async def get_response_cache_value(value):
    return "get_response_cache_value"


@response_inspect_router.get("/etag/{etag}")
async def get_response_etag():
    return "get_response_etag"


@response_inspect_router.get("/response-headers")
async def get_response_headers(response:Response):
    return {"headers": response.headers}


@response_inspect_router.post("/response-headers")
async def post_response_headers():
    return {"headers": response.headers}

