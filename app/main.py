from fastapi import FastAPI
from routers.forecast import router


app = FastAPI()

app.include_router(router)