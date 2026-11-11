import os
import time
import uuid
import json

class noticias:
    def __init__(self,url,status,id,titulo):
        self.url = url
        self.status = status
        self.id = id
        self.titulo = titulo

def random_id():   
    Id = uuid.uuid4().hex
    return Id

def status():

    print("Qual o status dessa notícia?:\n" \
        "[1] - Verdadeiro\n[2] - Falso\n[3] - Não checado")  #função para facilitar na checagem do status, evitando diferentes convenções de escrita
    Status = None
    while Status is None:
        opcao = input("")
        match opcao:
            case '1':
                Status = 'Verdadeiro'                    
            case '2':
                Status = 'Falso'                    
            case '3':
                Status = 'Não checado'                    
            case _:
                print('Insira um status válido!')
    return Status

def cadastrar_noticia():
    continuar = True
    while continuar:       
        Id = random_id()
        os.system('cls')
        print('==========CADASTRO DE NOTÍCIAS==========')        
        Url = input('url: ')
        Titulo = input('titulo: ')
        Status = status()
        news = noticias(Url,Status,Id,Titulo)
        nova_noticia = {
                    'Url': news.url,
                    'Título': news.titulo,
                    'Status': news.status
                    }
        try:
            with open('noticias.json', 'r', encoding='utf-8') as arquivo:
                noticias_dict = json.load(arquivo)
        except( FileNotFoundError, json.JSONDecodeError):
            noticias_dict = {}

        noticias_dict[Id] = nova_noticia

        with open("noticias.json", 'w', encoding="utf-8") as f:
            json.dump(noticias_dict, f, indent=4, ensure_ascii=False)


        print(f"✅ Notícia cadastrada e salva com sucesso!\nId registrado: {Id}")

        opcao = input('[1] - Continuar\n[2] - Voltar ao menu\n')
        match opcao:
            case '1':
                continuar = True                   
            case '2':
                continuar = False
                menu_principal()
            case _:
                print('Insira uma opção válida!')

def gerenciamento():
    #menu de gereciamento para a maniupulação das noticias(atualizar e excluir)
    os.system('cls')
    print("[1] - Atualizar notícias\n"
          "[2] - Excluir notícia\n"
          "[3] - Voltar ao menu\n")
    escolha = input()
    validar = True
    while validar:
        match escolha:
            case '1':
                validar = False
                atualizar_noticias()
            case '2':
                validar = False
                excluir_noticia()
            case '3':
                validar = False
                menu_principal()
            case _:
                os.system('cls')
                print("[1] - Atualizar notícias\n"
                        "[2] - Excluir notícia\n"
                        "[3] - Voltar ao menu\n")
                validar = input("Insira uma opção válida: \n")

def atualizar_noticias():
    #usuario esoclhe a noticia que deseja atualizar a partir do ID dela
    os.system('cls')    
    try:
        with open('noticias.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            if not dados:
                raise Exception
        
        num_id = input('Insira o ID da notícia que deseja atualizar: \n').strip() 
        if num_id in dados:
            dados[num_id]['Status'] = status()
            with open("noticias.json", 'w', encoding="utf-8") as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
            time.sleep(0.7)
            print("Notícia atualizada com sucesso!\n")
            time.sleep(2.5)
            gerenciamento()
        else:
            print("Notícia não encontrada.")

                
    except EOFError:
        print("\nNenhuma notícia foi encontrada!\n")
        print('Voltando ao menu...')
        time.sleep(2.5)
        menu_principal()

def excluir_noticia():
    os.system('cls')            
    try:
       with open('noticias.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            if not dados:
                raise Exception
        
            num_id = input('Insira o ID da notícia que deseja Excluir: \n').strip() 
            if dados.get(num_id):
                dados.pop(num_id)
                with open("noticias.json", 'w', encoding="utf-8") as f:
                    json.dump(dados, f, indent=4, ensure_ascii=False)
                time.sleep(0.7)
                print("Notícia excluida com sucesso!\n")
                time.sleep(2.5)
                gerenciamento()

            else:
                print("Notícia não encontrada.")
                    
    except :
            print("\nNenhuma notícia foi encontrada!\n")
            print('Voltando ao menu...')
            time.sleep(2.5)
            menu_principal()

def consultar_noticias():
    os.system('cls')
    print('==========CONSULTAR NOTÍCIAS==========')
    try:
        with open('noticias.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            for id, info in dados.items():
                print(f"ID: {id}\nTítulo: {info['Título']}\nURL: {info['Url']}\nStatus: {info['Status']}\n")


            if not dados:
                raise Exception
   
        print('\n[1] - Filtrar notícias por status' \
        '\n[2] - Filtrar notícias por título\n[3] - Voltar ao menu')
        verificando = True
        while verificando:
            opcao = input("Insira sua opção: ") 

            match opcao:
                case '1': 
                    os.system('cls')
                    Status = status()
                    print('Filtrando por status...')
                    time.sleep(0.7)
                    os.system('cls')
                    encontrado = None
                    try:
                        with open('noticias.json','r', encoding='utf-8') as arquivo:
                            dados = json.load(arquivo)
                            for id, info in dados.items():
                                if info['Status'] == Status:
                                    print(f"ID: {id}\nTítulo: {info['Título']}\nURL: {info['Url']}\nStatus: {info['Status']}\n")
                                    encontrado = True
                            if not encontrado:
                                print(f'Nenhuma notícia registrada com o status {Status}.')
                                time.sleep(2.0)
                                consultar_noticias()    
                    except FileNotFoundError:
                        print('Nenhuma notícia foi cadastrada ainda')                    
                    verificando = False
                
                    #Filtro por titulo/palavra-chave
                case '2':
                    os.system('cls')
                    encontrado = None
                    search = input('Digite o título: ').strip().lower()

                    os.system('cls')
                    print('Filtrando por titulo...')
                    time.sleep(0.7)
                    os.system('cls')

                   
                    with open('noticias.json','r', encoding='utf-8') as arquivo:
                        dados = json.load(arquivo)
                        for id, info in dados.items():
                            if info['Título'].lower().find(search) != -1 and len(search) > 1:
                                encontrado = True
                                print(f"ID: {id}\nTítulo: {info['Título']}\nURL: {info['Url']}\nStatus: {info['Status']}\n")
                            elif info['Título'].startswith(search):
                                encontrado = True
                                print(f"ID: {id}\nTítulo: {info['Título']}\nURL: {info['Url']}\nStatus: {info['Status']}\n")
                        if not encontrado:
                            print(f'Nenhuma notícia foi encontrada com o titulo {search}.')
                    
                    verificando = False   
                case '3':
                    verificando = False
                    menu_principal()
                case _:
                    opcao = input("Digite uma opção válida!: ")
    except:
        print("\nNenhuma notícia foi cadastrada ainda, cadastre a primeira notícia!\n")
        print('Voltando ao menu...')
        time.sleep(2.5)
        menu_principal()
    
def relatorio():
    os.system('cls')

    total_noticias, qtd_falso, qtd_verdadeiro, qtd_naochecado = 0, 0, 0, 0

    try:
        with open('noticias.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        for id, info in dados.items():
            total_noticias += 1
            if dados[id]["Status"] == "Verdadeiro":
                qtd_verdadeiro += 1
            if dados[id]["Status"] == "Falso":
                qtd_falso += 1
            if dados[id]["Status"] == "Não checado":
                qtd_naochecado += 1

        porcentagem_v = (100*qtd_verdadeiro)/total_noticias
        porcentagem_f = (100*qtd_falso)/total_noticias
        porcentagem_nc = (100*qtd_naochecado)/total_noticias

        print('==========RELATÓRIO==========\n')
        arquivo_relatorio = open('relatorio.txt', '+w', encoding='utf-8')
        arquivo_relatorio.write(f'Total de notícias: {total_noticias}\n')
        arquivo_relatorio.write(f'Verdadeiro {qtd_verdadeiro} --> {porcentagem_v:.2f}% do total \nNão checado {qtd_naochecado} --> {porcentagem_nc:.2f}% do total \nFalso {qtd_falso} --> {porcentagem_f:.2f}% do total')
        arquivo_relatorio.close()
        with open('relatorio.txt', 'r', encoding='utf-8') as arquivo_relatorio:
            for linha in arquivo_relatorio:
                print(linha, end= '')

    except :
        print("\nNenhuma notícia foi cadastrada ainda, cadastre a primeira notícia!\n")
        print('Voltando ao menu...')
        time.sleep(2.5)
        menu_principal()

def menu_principal():
    
    os.system('cls')
    print("====Sentinela da verdade====\n\n")
    print('[1] - Cadastrar uma notícia')
    print('[2] - Consultar notícias')
    print('[3] - Atualizar notícias')
    print('[4] - Gerar relatório')
    print('[5] - Encerrar\n')
    verificar = True
    while verificar:
        opcao = input('escolha uma opção: ')
        match opcao:
            case "1":
                os.system('cls')
                verificar = False
                print("função de cadastrar")
                cadastrar_noticia()
            case '2':
                verificar = False
                consultar_noticias()
                
            case '3':
                os.system('cls')
                verificar = False
                gerenciamento()
            case '4':
                os.system('cls')
                verificar = False
                relatorio()   
            case '5':
                print("\nEncerrando...")
                time.sleep(1.5)
                os.system('cls')
                verificar = False 
            case _:
                os.system('cls')
                print('[1] - Cadastrar uma notícia')
                print('[2] - Consultar notícias')
                print('[3] - Atualizar notícias')
                print('[4] - Gerar relatório')
                print('[5] - Encerrar\n')
                print('Insira uma opção válida! ')
    
menu_principal()

