def verifica_maior_idade():
    try:
        idade = int(input("Digite sua idade:"))
        if(idade >= 18):
            print("Maior idade")
        else:
            print("Menor idade")
    except:
        print("Valor inserido é invaldo!")
        verifica_maior_idade()


verifica_maior_idade()