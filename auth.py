from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/basic-auth/{user}/{passwd}")
async def get_auth_basic_auth(user, passwd):
    return {user: passwd}


@auth_router.get("/bearer")
async def get_auth_bearer():
    return "/bearer"


@auth_router.get("/digest-auth/{qop}/{user}/{passwd}")
async def get_auth_digest_auth(qop, user, passwd):
    return qop, user, passwd


@auth_router.get("/digest-auth/{qop}/{user}/{passwd}/{algorithm}")
async def get_auth_diget_auth_a(qop, user, passwd, algorithm):
    return qop, user, passwd, algorithm


@auth_router.get("/digest-auth/{qop}/{user}/{passwd}/{algorithm}/{stale_after}")
async def get_auth_diget_auth_a_s(qop, user, passwd, algorithm, stale_after):
    return qop, user, passwd, algorithm, stale_after


@auth_router.get("/hidden-basic-auth/{user}/{passwd}")
async def get_hidden_basic_auth(user, passwd):
    return {user: passwd}
