from fastapi import FastAPI
from router import general

app = FastAPI(title="ConvoApp",
              description="This is a chatting app where all the user can create group and char among themselves",
              version="1.0.0")

app.include_router(general.router, prefix="", tags=["General"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
