

def checknum(print, error):
    num = input(print)
    while True:
        if num.isnumeric():
            num = int(num)
            return num

        if num.isalpha():
            num = input(error)


def adicionar_produto(arquivo='lista.json'):
    lista = {}
    while True:
        while True:
            prod = input('Digite o Nome do Produto. ').strip().title()
            if check_produto(produto=prod) == False:
                break
            else:
                print('Esse Produto ja se encontra na lista')

        prec = checknum('Digite o Valor do Produto. ', 'Digite um valor inteiro')
        lista[prod] = prec
        esc = input('Adicionar mais produtos ?\n [S]Sim [N]Não : ').strip().upper()

        while not esc[0] in 'N':
            if esc[0] in 'S':
                break
            else:
                print('Desculpa nao entendi sua escolha')
                esc = input('Adicionar mais produtos ?\n [S]Sim [N]Não : ').strip().upper()
        if esc[0] in 'N':
            break
    return lista


def escrever(lista, arquivo='lista.json'):
    try:
        open(arquivo, 'x')
        listaj = open(arquivo, "a+")
    except:
        listaj = open(arquivo, "a+")

    for p, v in lista.items():
        print(f"{p} : {v}", file=listaj)


def check_produto(produto, arquivo = 'lista.json'):
    lista1 = open(arquivo, 'r')
    if produto.strip().title() in lista1.read():
        return True
    else:
        return False

a = adicionar_produto()



