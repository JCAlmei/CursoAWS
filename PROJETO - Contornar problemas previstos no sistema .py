print ("\nPara saber a sua idade, digite as informações abaixo.")
nome = (input("Nome completo: "))

rodar = True
while (rodar):

    
    print ("Ano de nascimento (1922-2022): ")

    try:

        nascimento = int(input())
        ano = 2022
        idade = ano - nascimento

        if (nascimento >= 1922) and (nascimento <= 2022):
            rodar = False
            print(f"\nOlá, {nome}!")
            print(f"Você completou ou completará {idade} anos em 2022.\n")

        else:
            print("\n('ERRO'_Ano de nascimento inferior a 1922 ou superior a 2022)")
            print("\nPor favor, digite novamente o seu ano de nascimento\n")

    except:

       print("\n('ERRO'_Caracter inválido)")
       print ("\nPor favor, digite novamente o seu ano de nascimento\n") 