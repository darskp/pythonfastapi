from fastapi import FastAPI, Request
from routers.users import router

app=FastAPI()
app.include_router(router)

# HTTP Middleware
@app.middleware("http")
async def log_requests(request:Request,call_next):
    print("PATH",request.url.path)
    response=await call_next(request)
    print("STATUS",response.status_code)
    return response

# Output
# PATH /my-settings
# STATUS 200
