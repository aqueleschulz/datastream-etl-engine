from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "active"

def test_upload_csv():
    csv_content = "id,produto,quantidade,valor_unitario,categoria\n1,Test,1,10.0,TestCat"
    files = {
        'file': ('teste.csv', csv_content, 'text/csv')
    }
    
    response = client.post("/v1/vendas/upload", files=files)
    
    assert response.status_code == 200
    data = response.json()
    assert data["receita_total"] == 10.0
    assert data["vendas_por_categoria"]["TestCat"] == 10.0

def test_upload_extensao_errada():
    files = {'file': ('teste.txt', 'conteudo', 'text/plain')}
    response = client.post("/v1/vendas/upload", files=files)
    assert response.status_code == 400