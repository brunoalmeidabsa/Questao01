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