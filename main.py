from fastapi import FastAPI
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
import uvicorn
from db.engine import engine
from sqlalchemy import text

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
  try:
    with engine.connect() as conn:
      conn.execute(text("SELECT 1"))
      print("Database connected successfully")
  except Exception as e:
    print(f"Error connecting to database: {e}")
    raise e
  yield
  print("Database disconnected successfully")

PORT = os.getenv("PORT", 4000)

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "ok"}


def main():
    uvicorn.run(app, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    main()
