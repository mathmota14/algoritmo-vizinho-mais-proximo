#Lê o arquivo texto que possui a matriz
arquivo = open("matriz.txt")
cod = arquivo.readlines()
lista = []

for dados in cod:
    a = dados.replace("\n", "")
    b = a.split(" ")
    lista.append(b)

#Irá descobrir a quantidade de linhas e colunas, além das coordenadas do restaurante e dos pontos de entrega
tamanho = lista.pop(0)
linha = int(tamanho[0])
coluna = int(tamanho[1])
coordenadas, local = [], []

for l in range(linha):
    for c in range(coluna):
        if lista[l][c] != "0":
            coordenadas.append((l, c))
            local.append(lista[l][c])

#Cria um dicionário para o restaurante e outro para os pontos de entrega
dicionario = dict(zip(local, coordenadas))
restaurante = {}
restaurante['R'] = dicionario.pop('R')

#Variável r que fica mudando cada vez que chega em um ponto de entrega e a variável rTemp fixa do restaurante
r = restaurante.get('R')
rTemp = restaurante.get('R')

partida, resultado, custo = 0, 0, 0
caminho = []

#Calcula o custo partindo do ponto R(restaurante) e passando pelo ponto de entrega que está mais próximo do atual
for t in range(len(coordenadas)):
    for u in range(len(dicionario)):
        partida += sum(tuple(map(lambda i, j: abs(i - j), r, list(dicionario.values())[u])))

        if resultado == 0 or partida <= resultado:
            resultado = partida
            rInicio = list(dicionario.values())[u]
            letraDesejada = list(dicionario)[u]
        partida = 0
        
    r = rInicio
    caminho.append(letraDesejada)
    custo += resultado
    resultado = 0
    del dicionario[letraDesejada]

    #Quando chega no último ponto de entrega o drone volta para o restaurante
    if len(dicionario) == 0:
        partida += sum(tuple(map(lambda i, j: abs(i - j), r, rTemp)))
        custo += partida
        break

#Mostra o menor custo com o melhor caminho a ser seguido
print("Menor custo:", custo)
print("Melhor caminho:", "R", ' '.join(caminho), "R")