from fastapi import FastAPI
import uvicorn

title_text = "DataStream ETL Engine"
version_text = "1.0.0"

app = FastAPI(title=title_text, version=version_text)

@app.get("/")
async def health_check():
    return {
        "status": "active",
        "service": title_text,
        "version": version_text
    }

if __name__ == "__main__":
    uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=True)