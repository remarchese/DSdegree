def calcularDistancia(cartAtual, cartVizinho):
    x = (cartAtual[0] - cartVizinho[0])**2 + (cartAtual[1] - cartVizinho[1])**2 + (cartAtual[2] - cartVizinho[2])**2 + (cartAtual[3] - cartVizinho[3])**2
    distancia = x**.5
    return distancia
# calcularDistancia((5800., 4000., 1200., 200.),(5900., 3000., 5100., 1800.))



def encontrarMaisProximos(k, pessoa, data):
    listProximos = []
    for v in range(len(data)):
        listProximos.append((data[v][1], calcularDistancia(pessoa[2], data[v][2])))
        if v >= k:
            listPerfisDistancias = list(zip(*listProximos))
            #print(listPerfisDistancias)
            #print(' ')
            idxMaior = listPerfisDistancias[1].index(max(listPerfisDistancias[1]))
            #print(idxMaior)
            #print(' ')
            listProximos.pop(idxMaior)
            #print(listProximos)
            #print(' ')
    return listProximos
# d = encontrarMaisProximos(5, [45926320819, '', (5800., 4000., 1200., 200.)], data)

def definirPerfil(listPerfisProximos):
    dicTotais = {
        'Conservador': 0,
        'Moderado': 0,
        'Agressivo': 0
    }
    # print(dicTotais)
    for perfil in listPerfisProximos:
        if perfil[0] == 'Conservador':
            dicTotais['Conservador'] += 1
        elif perfil[0] == 'Moderado':
            dicTotais['Moderado'] += 1
        else:
            dicTotais['Agressivo'] += 1
    print(dicTotais)
    totais = [dicTotais.get('Conservador'), dicTotais.get('Moderado'), dicTotais.get('Agressivo')]
    # print(totais)
    maior = max(totais)
    # print(maior)
    if (maior == dicTotais.get('Conservador')):
        return 'Conservador'
    elif (maior == dicTotais.get('Moderado')):
        return 'Moderado'
    else:
        return 'Agressivo'