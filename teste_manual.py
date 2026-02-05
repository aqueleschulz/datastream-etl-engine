import asyncio
from src.services.etl import processar_vendas_csv

async def main():
    path = "data/vendas_large.csv"
    print(f"Lendo arquivo local: {path}...")
    
    with open(path, "rb") as f:
        conteudo_bytes = f.read()
    
    print("Enviando para o Service Layer...")
    
    resultado = await processar_vendas_csv(conteudo_bytes)
    
    print("\n--- RELATÓRIO FINAL ---")
    print(resultado.model_dump_json(indent=2))

if __name__ == "__main__":
    asyncio.run(main())