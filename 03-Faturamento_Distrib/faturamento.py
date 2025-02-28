print("###### FATURAMENTO DISTRIBUIDORA ########")

import json
with open('./data/dados.json', 'r', encoding='utf-8') as file:
    dados = json.load(file)

# maiores que 0
valores = [d['valor'] for d in dados if d['valor'] > 0]

# menor e maior
menor_faturamento = min(valores)
maior_faturamento = max(valores)
print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")

# media
media = sum(valores) / len(valores)
dias_acima_media = len([v for v in valores if v > media])
print(f"Dias com faturamento acima da média: {dias_acima_media}")

