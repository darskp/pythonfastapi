from fastapi import FastAPI
from routes.users import router
app=FastAPI()
app.include_router(router)

@app.middleware("http")
async def log_request(request,call_next):
    print("request",request.url.path)
    response=await call_next(request)
    print("res",response.status_code)
    return response

