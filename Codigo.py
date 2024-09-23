
while True:
    carros = {
        'modelo': ['opala', 'marea', 'kombi', 'celtinha brabo', 'uno', 'monza', 'corcel'],
        'potência (cv)': [172, 130, 250, 140, 100, 120, 150],
        'consumo (km/l)': [1, 3, 8, 7, 15, 2, 1.5],
        'cor': ['laranja', 'verde', 'branca', 'preto', 'prata', 'preto', 'azul'],
        'ano': ['1972', '2004', '1985', '2014', '2001', '1980', '1975'],
        'estoque': [5, 6, 7, 8, 9, 10, 11],
        'preço(R$)': [50, 10, 2.50, 1000000, 100, 200, 999999]
    }
    def força_opção(msg, conjunto, msg_erro='Invalido'):
        opcoes = '\n'.join(conjunto)
        escolha = input(f'{msg}\n {opcoes} \n -->')
        while not escolha in conjunto:
            print(msg_erro)
            escolha = input(f'{msg} \n {opcoes} \n -->')
            return escolha


    indices = {}
    for i in range(len(carros['modelo'])):
        nome = carros['modelo'][i]
        indices[nome] = i
        print(indices)
    sim_ou_não = ['sim', 'não']



    def checa_numero(msg, msg_erro='Invalido'):
        num = input(msg)
        while not num.isnumeric():
            print(msg_erro)
            num = input(msg)
        return int(num)

    def cria_indices():
        indices={}
        for i in range (len(carros['modelo'])):
            nome = carros ['modelos'][i]





    def remover():
        escolha = força_opção('Qual carro você deseja remover', carros['modelo'])
        indice_escolha = indices[escolha]
        for key in carros.keys():
            carros[key].pop(indice_escolha)
        return
    def cadastrar():
        for key in carros.keys():
            info = input(f'Diga o novo {key}:')
            carros[key].append(info)
        return
    def atualizar():
        opcoes_atualização= ['Total', 'Especifica']
        escolha = força_opção('Qual carro você deseja atualizar?', carros['modelo'])
        indice_escolha = indices[escolha]
        tipo_atualização= força_opção('Todas informações ou só uma',['Total', 'Especifica'])
        if tipo_atualização == opcoes_atualização[0]:
            for key in carros .keys():
                info = input(f'Diga o novo {key}:')
                carros[key][indice_escolha]= info
        else:
            caracteristicas = força_opção('Ouqe será alterado',carros.keys())
            carros[caracteristicas] = input(f'Diga a nova {caracteristicas}')
        return
    def printa_dics(dic):
        for key in dic.keys():
            if type(dic[key]) is not dict:
                print(f'{key}: {dic[key]}')
            else:
                printa_dics(dic[key])




    carrinho = {
        'carros': {},
        'Valor Total(R$)': 0,
        'Endereço': {
            'Rua ': '',
            'Número': '',
            'Complemnto': '',
            'CEP': ''
        }
    }

    escolha = força_opção('Qual carro te interessa', carros, 'Invalido')
    indice_escolha= indices[escolha]
    for key in carros.keys():
        print(f'{key}: {carros[key][indice_escolha]}')
    comprar= força_opção(f'Você ira comprar o {escolha}',sim_ou_não)
    if comprar == sim_ou_não[0]:
        qtd = checa_numero(f'Quantas unidades de {escolha}? \n-->')
        if qtd > carros ['estoque'][indice_escolha]:
            print('Não há estoque suficiente')
            continue
        else:
            carros('estoque')[indice_escolha]-= qtd
            if escolha not in carrinho['carros'].keys():
                carrinho['carros'][escolha]= qtd
            else:
                carrinho['carros'][escolha]+=qtd
                carrinho['Valor Total(R$)']+= qtd*carros['preço(R$)'][indice_escolha]

        encerrar= força_opção('Você deseja encerrar a compra',sim_ou_não)
        if encerrar == sim_ou_não[0]:
            if carrinho ['Valor Total(R$)'] !=0:
                for key in carrinho ['Endereço'].keys():
                    info = input (f'Diga o/a {key}')
                    carrinho ['Endereço'][key] = info
            print(carrinho)
            break

    else:
        print('Tchau')
        break
lista =[172,130,250,140,100,120,150]
lista.pop(0)
opcoes_funcionario = ['Remover', 'Cadastrar','Adicionar', 'Sair']
print(lista)
usuario = ['Cliente','funcionario']
tipo_usuarios = força_opção('O que você é?', usuario)
if tipo_usuarios == usuario[0]:
    comprar()
else:
    operacao = força_opção('Qual operação será realizada', opcoes_funcionario)
    if operacao == opcoes_funcionario[0]:
        remover()
        indices = cria_indices()
    elif operacao == opcoes_funcionario [1]:
        cadastrar()
        indices = cria_indices()
    elif opcoes_funcionario ==opcoes_funcionario[2]:
        atualizar()
    else:
        print()


    import pandas as pd
    print(pd.DataFrame(carros))
    print(indices)
    pass
