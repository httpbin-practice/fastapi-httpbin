
from fastapi import Request

def get_base_resp(request:Request):
    resp = {
        "args":request.query_params,
        "headers":request.headers,
        "url":request.url._url,
        "method":request.method,
        "origin":request.client.host
    }
    if request.method.lower() != "get":
        resp["data"]= ""
        resp["files"]=""
        resp["form"]= ""
        resp["json"] = request.json
    return resp