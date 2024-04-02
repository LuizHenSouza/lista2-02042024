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

def verifica_par_ou_impar():
    try:
        valor = int(input("Digite um número:"))
        if(valor%2 == 0):
            print("O número é par")
        else:
            print("O número é ímpar")
    except:
        print("valor inserido é invalido")
        verifica_par_ou_impar()

verifica_par_ou_impar()