def cadastro(n):
    nome_arquivo = "GrupoDePessoas.txt"
    with open(nome_arquivo,"w",newline="") as arquivo:
        for i in range(n):
            nome = str(input("Digite o nome do usuário:"))
            celular = int(input("Digite o celular:"))
            if(i != n-1):
                arquivo.write(f"{nome.capitalize()} {celular}\n")
            else:
                arquivo.write(f"{nome.capitalize()} {celular}") 
    print("Cadastrado com sucesso")
    return nome_arquivo

def busca(nome_arquivo):
    try:
        with open(nome_arquivo,"r",newline="") as arquivo:
            nome = str(input("Digite o nome de quem você deseja encontrar:"))
            nome = nome.capitalize()
            
            matriz = []
            for linha in arquivo:
                linha = linha.rstrip("\n")
                matriz.append(linha.split(" "))

            achou = False
            for i in range(len(matriz)):
                if(matriz[i][0] == nome):
                    print(f"O numero de {nome} é {matriz[i][1]}")
                    achou = True

        if(not(achou)):
            print("Usuário não encontrado, verifique o nome escrito")
        else:
            print("Busca realizada com sucesso!")
    except:
        print("Arquivo não encontrado, realize o cadastro antes de acessar a busca")

def main():
    arquivo = "GrupoDePessoas.txt"
    a = int(input("Digite a opção:\n1-Cadastro\n2-Busca\n0-Exit\n"))
    
    if(a == 1):
        n = int(input("Digite quantos usuários deseja cadastrar:"))
        arquivo = cadastro(n)
        main()

    elif(a == 2):
    
        busca(arquivo)
        main()
    elif(a == 0):
        print("Execução finalizada!")
    else:
        print("opção inválida")
        main()

main()