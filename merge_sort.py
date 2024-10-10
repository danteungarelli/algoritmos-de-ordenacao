import time
import random


def gerar_lista(tamanho, tipo_distribuicao):
    if tipo_distribuicao == 1:
        return list(range(tamanho))
    elif tipo_distribuicao == 2:
        return list(range(tamanho, 0, -1))
    elif tipo_distribuicao == 3:
        return random.sample(range(tamanho), tamanho)


def merge_sort(arr):
    comparacoes = 0
    trocas = 0

    def merge(left, right):
        nonlocal comparacoes, trocas
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparacoes += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                trocas += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        return merge(left, right)

    sorted_arr = sort(arr)
    arr[:] = sorted_arr
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
    print(f"\nExecutando Merge Sort com uma lista de {tamanho} elementos ({distribucao_texto[tipo_distribuicao]}).\n")

    start_time = time.time()
    comparacoes, trocas = merge_sort(lista)
    end_time = time.time()

    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
    print(f"Número de comparações: {comparacoes}")
    print(f"Número de trocas: {trocas}")

if __name__ == "__main__":
    main()
