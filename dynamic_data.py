from fastapi import APIRouter

dynamic_data_router = APIRouter(prefix="/dynamic-data", tags=["Dyncmic Data"])


@dynamic_data_router.get("/base64/{value}")
async def get_base64_value(value):
    return value


@dynamic_data_router.get("/bytes/{n}")
async def get_bytes_n(n):
    return n


@dynamic_data_router.delete("/delay/{delay}")
async def delete_delay_delay(delay):
    return delay


@dynamic_data_router.get("/delay/{delay}")
async def get_delay_delay(delay):
    return delay


@dynamic_data_router.patch("/delay/{delay}")
async def patch_delay_delay(delay):
    return delay


@dynamic_data_router.post("/delay/{delay}")
async def post_delay_delay(delay):
    return delay


@dynamic_data_router.put("/delay/{delay}")
async def put_delay_delay(delay):
    return delay


@dynamic_data_router.get("/drip")
async def get_drip():
    return "get_drip"


@dynamic_data_router.get("/links/{n}/{offset}")
async def get_links(n, offset):
    return n, offset


@dynamic_data_router.get("/range/{numbytes}")
async def get_range(numbytes):
    return numbytes


@dynamic_data_router.get("/stream-bytes/{n}")
async def get_stream_bytes(n):
    return n


@dynamic_data_router.get("/stream/{n}")
async def get_stream(n):
    return n


@dynamic_data_router.get("/uuid")
async def get_uuid():
    return "get_uuid"
