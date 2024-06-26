from fastapi import FastAPI
from routers import (
    router_account, router_posts
)

app = FastAPI()
app.include_router(router_account.router)
app.include_router(router_posts.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
