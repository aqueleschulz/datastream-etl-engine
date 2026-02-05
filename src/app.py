from fastapi import FastAPI, File, UploadFile, HTTPException
from src.domain.schemas import RelatorioFinal
from src.services.etl import processar_vendas_csv
import uvicorn

title_text = "DataStream ETL Engine"
version_text = "1.0.0"

app = FastAPI(title=title_text, version=version_text)

@app.get("/", tags=["Health"])
async def health_check():
    return {
        "status": "active",
        "service": title_text,
        "version": version_text
    }

@app.post("/v1/vendas/upload", response_model=RelatorioFinal, tags=["ETL"])
async def upload_vendas(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="O arquivo deve ser um CSV.")

    try:
        content = await file.read()
        
        resultado = await processar_vendas_csv(content)
        
        return resultado

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=True)