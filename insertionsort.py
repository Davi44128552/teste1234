# Criando o vetor
vetor = [42, 17, 85, 23, 56, 31, 70, 10, 94, 8]
print(vetor)

# Insertion-Sort
    # Loop principal, feito para percorrer os subvetores
for j in range(1, 10):

    # Guardar determinado valor em uma variável e criar uma variável para adicionar o termo anterior
    termo = vetor[j]
    i = j - 1

    # Criação de outro loop para verificar se o termo anterior é maior que o seu sucessor
    while i >= 0 and termo < vetor[i]:
        vetor[i + 1] = vetor[i]
        vetor[i] = termo

        i -= 1

# Saída do algoritmo
print(vetor)
