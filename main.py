from fastapi import FastAPI
from routers import (
    router_account,
)

app = FastAPI()
app.include_router(router_account.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
