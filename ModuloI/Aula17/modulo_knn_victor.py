# Colocando as Funções do Victor

# Função para calcular a distancia entre os pontos e retornar uma lista, com todos esses resultados
def distancia(index, invest_definido, invest_nao_definido):
    ''' Essa função calcula a distancia entre dois pontos
    Entrada: index, carteira (tupla)
    Saída: lista de distancias
    '''
    resultado_distancia = 0
    lista_distancias = []
    
    for elemento in range(4): # 4 coordendas, ou investimentos
        resultado_distancia += (invest_definido[elemento] - invest_nao_definido[elemento])**2
    
    lista_distancias.append(index)    
    lista_distancias.append(resultado_distancia ** 0.5)
    return lista_distancias
    
#Função para ordenar e devolver apenas os 5 menores elementos
def valores_proximos(valores, k):
    return sorted(valores, key=lambda x:x[1])[:k]
    
#Função para definir o tipo de investimento do usuario
def definir_tipo_investimento(valores, data_com_index):
    lista_tipo_investimento = []
    
    for index, distancia in valores:
        lista_tipo_investimento.append(data_com_index[index][1][1])
    
    return max(set(lista_tipo_investimento), key = lista_tipo_investimento.count)   
    
#Função para retornar um dicionario com os CPF e o tipo de investimento ideal para os novos usuarios
def dicionario_usuario_investimento(cpf1, investimento_ideal, novos_usuarios):
    novos_usuarios[cpf1] = investimento_ideal
    
    return novos_usuarios