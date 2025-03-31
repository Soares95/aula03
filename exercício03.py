nome = input("Digite seu nome:")
idade = input("Digite sua idade:")
salario = float(input("Digite seu salario:"))

print(f"seu nome é {nome}, Qual a sua idade {idade}, Qual o seu salario {salario}")

percentual = float (input("Quantos porcentos você quer aumentar o seu salario"))
valordoauamento = float (percentual*salario/100)
novosalario = salario+valordoauamento

print(f"Olá {nome} voce tem {idade}, anos, seu salario atual é {novosalario:.2f}")