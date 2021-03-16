from fastapi import APIRouter

request_insepct_router = APIRouter(prefix="/request_inspect", tags=["Request Inspection"])


@request_insepct_router.get("/headers")
async def get_request_headers():
    return "get_request_headers"


@request_insepct_router.get("/ip")
async def get_request_ip():
    return "get_request_ip"


@request_insepct_router.get("/user-agent")
async def get_request_user_agent():
    return "get_request_user_agent"
