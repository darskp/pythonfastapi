from fastapi import FastAPI
from routes.users import router
from strawberry.fastapi import GraphQLRouter
from graphql_schema import schema

app=FastAPI()
app.include_router(router)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app,prefix="/graphql")

@app.middleware("http")
async def log_request(request,call_next):
    print("request",request.url.path)
    response=await call_next(request)
    print("res",response.status_code)
    return response

