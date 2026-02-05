import pytest
from src.services.etl import processar_vendas_csv

CSV_TESTE = """id_transacao,produto,quantidade,valor_unitario,categoria
1,Mouse,10,20.00,Perifericos
2,Teclado,5,50.00,Perifericos
3,Monitor,2,500.00,Monitores
""".encode('utf-8')

@pytest.mark.asyncio
async def test_calculo_agregacao():
    
    resultado = await processar_vendas_csv(CSV_TESTE)

    assert resultado.status == "sucesso"
    assert resultado.total_processado == 17
    
    assert resultado.vendas_por_categoria["Perifericos"] == 450.00
    
    assert resultado.vendas_por_categoria["Monitores"] == 1000.00

@pytest.mark.asyncio
async def test_arquivo_vazio_ou_invalido():
    csv_ruim = """id,prod,qtd,val,cat
    1,Mouse,DEZ,20.00,Perifericos
    """.encode('utf-8')
    
    with pytest.raises(Exception):
        await processar_vendas_csv(csv_ruim)