from pydantic import BaseModel, PositiveInt, PositiveFloat, Field

class VendaInput(BaseModel):
    id_transacao: str
    produto: str
    quantidade: PositiveInt = Field(..., description="Quantidade de produtos vendidos")
    valor_unitario: PositiveFloat = Field(..., description="Valor unitário do produto vendido")
    categoria: str

class RelatorioFinal(BaseModel):
    status: str
    total_processado: int
    receita_total: float
    vendas_por_categoria: dict[str, float]