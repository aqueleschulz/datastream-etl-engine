from csv import DictReader
from io import StringIO
from src.domain.schemas import RelatorioFinal

async def processar_vendas_csv(file_content: bytes) -> RelatorioFinal:
    decoded_content = file_content.decode('utf-8')
    
    file_in_memory = StringIO(decoded_content)
    reader = DictReader(file_in_memory)
    
    vendas_por_categoria = {}
    total_itens = 0
    receita_acumulada = 0.0

    for row in reader:
        try:
            qtd = int(row['quantidade'])
            preco = float(row['valor_unitario'])
            categoria = row['categoria']
            
            valor_venda = qtd * preco
            
            if categoria not in vendas_por_categoria:
                vendas_por_categoria[categoria] = 0.0
            
            vendas_por_categoria[categoria] += valor_venda
            
            total_itens += qtd
            receita_acumulada += valor_venda
            
        except Exception as e:
            print(f"\n[ERRO FATAL] Falha ao processar linha:")
            print(f"Conteúdo da Linha: {row}")
            print(f"Tipo do Erro: {type(e)}")
            print(f"Mensagem: {e}")
            raise e

    return RelatorioFinal(
        status="sucesso",
        total_processado=total_itens,
        receita_total=round(receita_acumulada, 2),
        vendas_por_categoria={k: round(v, 2) for k, v in vendas_por_categoria.items()}
    )