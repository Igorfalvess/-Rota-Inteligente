import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from scipy.spatial.distance import euclidean

# ====================================================
# ETAPA 1 - AGRUPAMENTO DE PEDIDOS (K-MEANS)
# ====================================================

# Parâmetros de entrada
TOTAL_PEDIDOS = 30
TOTAL_ENTREGADORES = 5
LAT_SEDE, LON_SEDE = -23.5520, -46.6345  # Exemplo: São Paulo (ligeiramente alterado)

print("=== ETAPA 1: AGRUPAMENTO DE PEDIDOS ===")

# Geração de dados simulados
np.random.seed(24)  # Mudança da semente
dados = {
    'Pedido_ID': range(1, TOTAL_PEDIDOS + 1),
    'Latitude': np.random.normal(LAT_SEDE, 0.07, TOTAL_PEDIDOS),
    'Longitude': np.random.normal(LON_SEDE, 0.09, TOTAL_PEDIDOS)
}
df = pd.DataFrame(dados)

# Execução do K-Means
coordenadas = df[['Latitude', 'Longitude']].values
modelo_kmeans = KMeans(n_clusters=TOTAL_ENTREGADORES, random_state=1, n_init='auto')
df['Rota_ID'] = modelo_kmeans.fit_predict(coordenadas)

print(f"Foram gerados {TOTAL_PEDIDOS} pedidos e agrupados em {TOTAL_ENTREGADORES} rotas.")

# Centroides (opcional)
centros = modelo_kmeans.cluster_centers_

# Visualização
plt.figure(figsize=(9, 7))
plt.scatter(df['Longitude'], df['Latitude'], c=df['Rota_ID'], cmap='plasma', s=90, edgecolors='white')
plt.scatter(LON_SEDE, LAT_SEDE, color='red', marker='s', s=300, label='Sede')
plt.title('Distribuição e Agrupamento de Entregas (K-Means)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('agrupamento_entregas.png')
plt.show()

# ====================================================
# ETAPA 2 - OTIMIZAÇÃO DE ROTAS (HEURÍSTICA)
# ====================================================

print("\n=== ETAPA 2: OTIMIZAÇÃO DE ROTAS ===")

def distancia(ponto1, ponto2):
    """Distância euclidiana entre dois pontos (Lat, Lon)."""
    return euclidean(ponto1, ponto2)

def gerar_rota_otimizada(pontos, sede):
    """
    Heurística do Vizinho Mais Próximo (Nearest Neighbor)
    para uma sequência simples de entregas.
    """
    lista_pontos = [tuple(p) for p in pontos.tolist()]
    rota = [sede]
    total = 0.0

    while lista_pontos:
        atual = rota[-1]
        distancias = [distancia(atual, p) for p in lista_pontos]
        prox = lista_pontos.pop(np.argmin(distancias))
        total += distancia(atual, prox)
        rota.append(prox)
    
    # Volta para a sede
    total += distancia(rota[-1], sede)
    rota.append(sede)

    rota_df = pd.DataFrame(rota, columns=['Latitude', 'Longitude'])
    return rota_df, total

# Geração das rotas
rotas = []
dist_total = 0
resumo_rotas = {}

print("Resumo de distâncias (por entregador):")
for i in range(TOTAL_ENTREGADORES):
    pontos_cluster = df[df['Rota_ID'] == i][['Latitude', 'Longitude']].values
    rota_df, dist = gerar_rota_otimizada(pontos_cluster, (LAT_SEDE, LON_SEDE))
    rota_df['Rota_ID'] = i
    rotas.append(rota_df)
    dist_total += dist
    resumo_rotas[i] = {'Paradas': len(pontos_cluster), 'Distância': f"{dist:.3f}"}
    print(f"Entregador {i}: {len(pontos_cluster)} entregas, distância total = {dist:.3f}")

print(f"\nDistância total geral: {dist_total:.3f}")

# Plotagem das rotas
todas_rotas = pd.concat(rotas, ignore_index=True)
cores = plt.cm.get_cmap('plasma', TOTAL_ENTREGADORES)

plt.figure(figsize=(10, 8))
for i in range(TOTAL_ENTREGADORES):
    r = todas_rotas[todas_rotas['Rota_ID'] == i]
    plt.plot(r['Longitude'], r['Latitude'], marker='o', linestyle='-', 
             linewidth=2, color=cores(i), label=f'Entregador {i}')
    pontos = df[df['Rota_ID'] == i]
    plt.scatter(pontos['Longitude'], pontos['Latitude'], s=120, edgecolors='black', color=cores(i))

plt.scatter(LON_SEDE, LAT_SEDE, marker='s', color='red', s=400, label='Sede', edgecolors='black')
plt.title('Rotas Otimizadas (Heurística do Vizinho Mais Próximo)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('rotas_otimizadas.png')
plt.show()

# Saída final para README
print("\n=== DADOS PARA README ===")
for i, r in resumo_rotas.items():
    print(f"Entregador {i}: Paradas={r['Paradas']}, Distância={r['Distância']}")
print(f"Distância Total: {dist_total:.3f}")
