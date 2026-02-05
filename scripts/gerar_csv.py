import csv
import random
import os

NUM_LINHAS = 100_000
ARQUIVO_SAIDA = "data/vendas_large.csv"

PRODUTOS = [
    ("Notebook", "Eletronicos", 4500.00),
    ("Smartphone", "Eletronicos", 2500.00),
    ("Mouse", "Perifericos", 150.00),
    ("Teclado", "Perifericos", 200.00),
    ("Cadeira", "Moveis", 800.00),
    ("Mesa", "Moveis", 1200.00),
]

def gerar_dados():
    os.makedirs(os.path.dirname(ARQUIVO_SAIDA), exist_ok=True)
    
    print(f"Gerando {NUM_LINHAS} linhas em '{ARQUIVO_SAIDA}'...")
    
    with open(ARQUIVO_SAIDA, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id_transacao", "produto", "quantidade", "valor_unitario", "categoria"])
        
        for i in range(NUM_LINHAS):
            prod, cat, preco_base = random.choice(PRODUTOS)
            preco_final = round(preco_base * random.uniform(0.9, 1.1), 2)
            qtd = random.randint(1, 10)
            
            writer.writerow([
                f"TXN-{i+1000}",
                prod,
                qtd,
                preco_final,
                cat
            ])
            
    print("Concluído!")

if __name__ == "__main__":
    gerar_dados()