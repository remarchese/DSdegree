def perfil_investidor(data,no_class, K):
    for i in range(len(no_class)):
        listadist = [] # lista apenas com as distancias
        listaNumerada = [] # lista com distancia e seus numeros
        listaOrdem = [] # lista em ordem de menor para maior

         # numero do no class


        for H in range(len(data)):
            x2 = data[H][2][0]
            y2 = data[H][2][1]   # os 120 cpf's classificados
            z2 = data[H][2][2]
            n2 = data[H][2][3]

            x1 = no_class[i][2][0]
            y1 = no_class[i][2][1]     # primeiro cpf do nao classificado 
            z1 = no_class[i][2][2]
            n1 = no_class[i][2][3]


            distancia = (((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2 + (n1-n2)**2)**0.5)# , data[H][1]   # calculo de distancia

            listadist.append(distancia)
            listaNumerada = list(enumerate(listadist))    # lista de distancias e a mesma já numerada




        for key, value in enumerate(listadist):       
            listaOrdem.append((value,key))                    # fazendo a lista do menor para o maior


        listaOrdem = sorted(listaOrdem)  # pegando os 5 menores
        #print(listaOrdem[:K])

        #####

        listaPerfis = []
        for value,key in listaOrdem:
            Q = key
            listaPerfis.append(data[Q][1])  # pega os perfis

        listaResultado = []
        lista5menores = listaPerfis[:K] # lista com os 5 menores perfis

        if lista5menores.count('Moderado') > lista5menores.count('Agressivo') and lista5menores.count('Moderado') > lista5menores.count('Conservador'):
            listaResultado.append((no_class[i][0],'Moderado'))

        if lista5menores.count('Agressivo') > lista5menores.count('Moderado') and lista5menores.count('Agressivo') > lista5menores.count('Conservador'):
            listaResultado.append((no_class[i][0],'Agressivo'))

        if lista5menores.count('Conservador') > lista5menores.count('Moderado') and lista5menores.count('Conservador') > lista5menores.count('Agressivo'):
            listaResultado.append((no_class[i][0],'Conservador'))

        print(listaResultado)