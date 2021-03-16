import time
import base64
import uuid
from fastapi import APIRouter,Request
from base import get_base_resp

dynamic_data_router = APIRouter(prefix="/dynamic-data", tags=["Dyncmic Data"])


@dynamic_data_router.get("/base64/{value}")
async def get_base64_value(value:str="SFRUUEJJTiBpcyBhd2Vzb21l"):
    resp_text = "Incorrect Base64 data try: SFRUUEJJTiBpcyBhd2Vzb21l"
    try:
        resp_text = base64.decodebytes(value.encode(encoding="utf-8"))
    except Exception as e:
        print(e)
    
    return resp_text


@dynamic_data_router.get("/bytes/{n}")
async def get_bytes_n(n:int,request:Request):
    return get_base_resp(request)


@dynamic_data_router.delete("/delay/{delay}")
async def delete_delay_delay(delay:int,request:Request):
    if delay< 0 or delay> 10:
        return "invalid:delay must 0<=delay<10"
    time.sleep(delay)     
    return get_base_resp(request)


@dynamic_data_router.get("/delay/{delay}")
async def get_delay_delay(delay:int,request:Request):
    if delay< 0 or delay> 10:
        return "invalid:delay must 0<=delay<10"
    time.sleep(delay)    
    return get_base_resp(request)


@dynamic_data_router.patch("/delay/{delay}")
async def patch_delay_delay(delay:int,request:Request):
    if delay< 0 or delay> 10:
        return "invalid:delay must 0<=delay<10"
    time.sleep(delay)    
    return get_base_resp(request)


@dynamic_data_router.post("/delay/{delay}")
async def post_delay_delay(delay:int,request:Request):
    if delay< 0 or delay> 10:
        return "invalid:delay must 0<=delay<10"
    time.sleep(delay)      
    return get_base_resp(request)


@dynamic_data_router.put("/delay/{delay}")
async def put_delay_delay(delay:int,request:Request):
    if delay< 0 or delay> 10:
        return "invalid:delay must 0<=delay<10"
    time.sleep(delay)    
    return get_base_resp(request)


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
    return {"uuid":uuid.uuid4()}
