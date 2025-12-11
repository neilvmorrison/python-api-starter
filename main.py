from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv("PORT", 4000)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": os.getenv("OTHER_ENV_VARIABLE")}


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    main()
