import time
import random

# Função para gerar listas de acordo com a distribuição escolhida
def gerar_lista(tamanho, tipo_distribuicao):
    if tipo_distribuicao == 1:
        # Lista ordenada
        return list(range(tamanho))
    elif tipo_distribuicao == 2:
        # Lista inversamente ordenada
        return list(range(tamanho, 0, -1))
    elif tipo_distribuicao == 3:
        # Lista aleatória
        return random.sample(range(tamanho), tamanho)

# Implementação do Selection Sort 
def selection_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0
    for i in range(n):
        # Encontrar o menor elemento no subarray não ordenado
        min_idx = i
        for j in range(i+1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Trocar o menor elemento com o primeiro elemento do subarray não ordenado
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1
    return comparacoes, trocas

# Função principal
def main():
    # Menu para escolha do tamanho do vetor
    print("Escolha o tamanho do vetor:")
    print("[1] 1.000 elementos")
    print("[2] 10.000 elementos")
    print("[3] 50.000 elementos")
    print("[4] 100.000 elementos")
    tamanho_escolhido = int(input("Digite o número correspondente ao tamanho do vetor: "))

    tamanhos = {1: 1000, 2: 10000, 3: 50000, 4: 100000}
    tamanho = tamanhos.get(tamanho_escolhido, 1000)  # Tamanho padrão de 1.000 se entrada for inválida

    # Menu para escolha da distribuição
    print("Escolha a distribuição dos elementos:")
    print("[1] Lista ordenada")
    print("[2] Lista inversamente ordenada")
    print("[3] Lista aleatória")
    tipo_distribuicao = int(input("Digite o número correspondente ao tipo de distribuição: "))
    
    distribucao_texto = {
        1: "ordenada",
        2: "inversamente ordenada",
        3: "aleatória"
    }
    

    # Gerar a lista com base na escolha
    lista = gerar_lista(tamanho, tipo_distribuicao)
    print(f"\nExecutando Selection Sort com uma lista de {tamanho} elementos ({distribucao_texto[tipo_distribuicao]}).\n")

    # Medir o tempo de execução
    start_time = time.time()
    comparacoes, trocas = selection_sort(lista)
    end_time = time.time()

    # Mostrar resultados
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
    print(f"Número de comparações: {comparacoes}")
    print(f"Número de trocas: {trocas}")

# Executar o código
if __name__ == "__main__":
    main()
