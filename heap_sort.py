import time
import random


def gerar_lista(tamanho, tipo_distribuicao):
    if tipo_distribuicao == 1:
        return list(range(tamanho))
    elif tipo_distribuicao == 2:
        return list(range(tamanho, 0, -1))
    elif tipo_distribuicao == 3:
        return random.sample(range(tamanho), tamanho)


def heap_sort(arr):
    comparacoes = 0
    trocas = 0

    def heapify(n, i):
        nonlocal comparacoes, trocas
        largest = i 
        left = 2 * i + 1  
        right = 2 * i + 2  

        
        if left < n and arr[left] > arr[largest]:
            largest = left
        comparacoes += 1

        
        if right < n and arr[right] > arr[largest]:
            largest = right
        comparacoes += 1

       
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  
            trocas += 1
            
            heapify(n, largest)

    def sort():
        nonlocal comparacoes, trocas
        n = len(arr)

        
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  
            trocas += 1
            heapify(i, 0)

    sort()
    return comparacoes, trocas


def main():
    print("Escolha o tamanho do vetor:")
    print("[1] 1.000 elementos")
    print("[2] 10.000 elementos")
    print("[3] 50.000 elementos")
    print("[4] 100.000 elementos")
    tamanho_escolhido = int(input("Digite o número correspondente ao tamanho do vetor: "))

    tamanhos = {1: 1000, 2: 10000, 3: 50000, 4: 100000}
    tamanho = tamanhos.get(tamanho_escolhido, 1000)

    print("Escolha a distribuição dos elementos:")
    print("[1] Lista ordenada")
    print("[2] Lista inversamente ordenada")
    print("[3] Lista aleatória")
    tipo_distribuicao = int(input("Digite o número correspondente ao tipo de distribuição: "))

    distribucao_texto = {1: "ordenada", 2: "inversamente ordenada", 3: "aleatória"}

    lista = gerar_lista(tamanho, tipo_distribuicao)
    print(f"\nExecutando Heap Sort com uma lista de {tamanho} elementos ({distribucao_texto[tipo_distribuicao]}).\n")

    start_time = time.time()
    comparacoes, trocas = heap_sort(lista)
    end_time = time.time()

    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
    print(f"Número de comparações: {comparacoes}")
    print(f"Número de trocas: {trocas}")

if __name__ == "__main__":
    main()
