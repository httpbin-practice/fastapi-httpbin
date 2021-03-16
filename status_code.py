from fastapi import APIRouter,Request,Response, status
from base import get_base_resp

status_router = APIRouter(prefix="/status", tags=["status"])

def get_status_return(codes,response:Response):
    code_str = f"_{str(codes)}_"
    for k,v in status.__dict__.items():
        if code_str in k:
            response.status_code = v
            return
    else:
        return "invalid status code"
@status_router.get("/{codes}")
async def get_status(codes, response:Response):
    return get_status_return(codes,response)


@status_router.delete("/{codes}")
async def delete_status(codes,response:Response):
    return get_status_return(codes,response)
    


@status_router.put("/{codes}")
async def put_status(codes,response:Response):
    return get_status_return(codes,response)
    


@status_router.post("/{codes}")
async def post_status(codes,response:Response):
    return get_status_return(codes,response)
    


@status_router.patch("/{codes}")
async def patch_status(codes,response:Response):
    return get_status_return(codes,response)
    
