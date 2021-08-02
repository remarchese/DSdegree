# Definir um valor para K
def define_k():
    k = int(input("Insira valor para k do modelo: "))
    return k

def calcular_distancia(ponto, data):
    all_distancias = []
    for j in range(len(data)): #varre todos os pontos estabelecidos
        dist_1 = ponto[2][0] - data[j][2][0]
        dist_2 = ponto[2][1] - data[j][2][1]
        dist_3 = ponto[2][2] - data[j][2][2]
        dist_4 = ponto[2][3] - data[j][2][3]
        distancia = (((dist_1**2)+(dist_2**2)+(dist_3**2)+(dist_4**2))**0.5)
        all_distancias.append(distancia)
    return all_distancias

def k_vizinhos(all_distancias, k):
    lista_enumerada = (list(enumerate(all_distancias)))
    lista_nova = []
    for i in range(len(lista_enumerada)):
        lista_nova.append(list(lista_enumerada[i]))

    for i in range(len(lista_enumerada)):
        lista_temp = lista_nova[i]
        lista_temp.reverse()
        lista_nova[i] = lista_temp

    lista_nova.sort()
    vizinho = []

    for i in range(k):
        vizinho.append(min(lista_nova))
        lista_nova.pop(0)
    return vizinho

def classifica_no_class(vizinho,k,data):

    moderado = 0
    conservador = 0
    agressivo = 0

    for i in range(k):
        if data[vizinho[i][1]][1] == 'Moderado':
            moderado+=1
        if data[vizinho[i][1]][1] == 'Conservador':
            conservador+=1
        if data[vizinho[i][1]][1] == 'Agressivo':
            agressivo+=1
   
    if conservador>moderado and conservador>agressivo:
        classicacao = 'Conservador'
    if moderado>conservador and moderado>agressivo:
        classicacao = 'Moderado'
    if agressivo>moderado and agressivo>conservador:
        classicacao = 'Agressivo'
    else:
        classicacao = data[vizinho[0][1]][1]
    
    return classicacao
