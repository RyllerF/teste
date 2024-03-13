#insira elementos separados por espaço
lista = input().split()
inversa = []

#começa na ultima posicao -1 para tirar o indice 0, vai até a posicao -1, e da direita pra esquerda
for i in range(len(lista) - 1, -1, -1):
   inversa.append(lista[i])
   
print(inversa)





