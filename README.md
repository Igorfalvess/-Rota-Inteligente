# -Rota-Inteligente
Otimização de Entregas com K-Means e Heurística

## 📖 Descrição do Projeto

Este projeto tem como objetivo **otimizar rotas de entrega** a partir de dados simulados de pedidos, utilizando duas etapas principais:

1. **Agrupamento Geográfico (K-Means)** – Agrupa os pedidos de entrega com base na proximidade entre eles.  
2. **Otimização de Rota (Heurística do Vizinho Mais Próximo)** – Determina uma sequência de visita aos pontos de entrega que minimiza a distância total percorrida por cada entregador.

O sistema simula o funcionamento de uma empresa de entregas que busca reduzir o tempo e o custo de deslocamento, aplicando algoritmos de **inteligência artificial** e **ciência de dados**.

---

## ⚙️ Parâmetros da Simulação

| Parâmetro | Valor |
|------------|--------|
| Total de Pedidos | **30** |
| Total de Entregadores | **5** |
| Localização da Sede | Latitude: `-23.5520`, Longitude: `-46.6345` |
| Semente Aleatória | `24` |
| Desvio (Latitude) | `0.07` |
| Desvio (Longitude) | `0.09` |

---

## 🧮 Etapa 1 – Agrupamento com K-Means

Nesta etapa, os pedidos são agrupados de acordo com a sua localização geográfica, gerando **5 clusters**, cada um representando a área de atuação de um entregador.

**Gráfico gerado:** `agrupamento_entregas.png`  
Mostra a distribuição dos pedidos e o ponto da sede em destaque.

**Resultados:**
- Total de pedidos gerados: **30**
- Total de agrupamentos (rotas): **5**

---

## 🚴‍♂️ Etapa 2 – Otimização de Rotas (Heurística Nearest Neighbor)

Após o agrupamento, cada conjunto de pedidos é otimizado individualmente por meio da heurística do **Vizinho Mais Próximo (Nearest Neighbor)**, que seleciona o ponto mais próximo a cada passo, retornando à sede ao final do percurso.

**Gráfico gerado:** `rotas_otimizadas.png`

### 🔢 Resultados Simulados

| Entregador | Pedidos | Distância Total |
|-------------|----------|-----------------|
| Entregador 0 | 6 | 0.5782 |
| Entregador 1 | 7 | 0.6654 |
| Entregador 2 | 5 | 0.6129 |
| Entregador 3 | 6 | 0.5971 |
| Entregador 4 | 6 | 0.6317 |
| **Total Geral** | **30** | **3.0853** |

> 💬 As distâncias são calculadas em **unidades euclidianas** (não correspondem a quilômetros reais).

---

## 📈 Visualização

Os gráficos salvos automaticamente pelo script mostram:
- **agrupamento_entregas.png** – Distribuição dos pedidos e agrupamento por cor.  
- **rotas_otimizadas.png** – Trajeto otimizado de cada entregador, com a sede marcada em vermelho.

---

## 🧠 Tecnologias Utilizadas

- **Python 3**
- **NumPy** – geração de dados aleatórios  
- **Pandas** – manipulação de dados  
- **Scikit-learn** – algoritmo K-Means  
- **Matplotlib** – geração dos gráficos  
- **SciPy** – cálculo de distâncias euclidianas  

---

## 🧩 Conclusão

O projeto demonstrou a eficiência de combinar **agrupamento geográfico (K-Means)** com **heurísticas simples de otimização** para reduzir a distância total percorrida nas entregas.

A distância total simulada foi de **aproximadamente 3.08 unidades**, mostrando que o agrupamento contribui para rotas mais curtas e equilibradas entre os entregadores.

---

## 👨‍💻 Autor

**Igor Ferreira Alves**  
Engenharia da Computação — UNIFECAF  
2025
