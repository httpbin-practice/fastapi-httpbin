from fastapi import APIRouter,Request,Header

request_insepct_router = APIRouter(prefix="/request_inspect", tags=["Request Inspection"])


@request_insepct_router.get("/headers")
async def get_request_headers(request:Request):
    return {"headers":request.headers}


@request_insepct_router.get("/ip")
async def get_request_ip(request:Request):
    return {"origin":request.client.host}


@request_insepct_router.get("/user-agent")
async def get_request_user_agent(request:Request):
    return {"User-Agent":request.headers.get("User-Agent")}
