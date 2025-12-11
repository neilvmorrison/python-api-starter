from fastapi import FastAPI
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
  try:
      print("Lifespan startup")
  except Exception as e:
    print(f"Error in lifespan: {e}")
    raise e
  yield
  print("Lifespan shutdown")

PORT = os.getenv("PORT", 4000)

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": os.getenv("OTHER_ENV_VARIABLE")}


def main():
    uvicorn.run(app, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    main()
