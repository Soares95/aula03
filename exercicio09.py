tipo = input("Qual foi o conbustivel?\n"
             " G - gasolina"
             " E - Etanol")

qtdlitros = float (input("Quantos litros foram abastecidos?"))
if tipo == "G" or tipo == "g" :
    valor = qtdlitros*5.8
else:
    if tipo == "E" or tipo == "e" :
        valor = qtdlitros*4.9
        print(f"Caro cliente voce abasteceu "
      f"{qtdlitros} e gastou R${valor:.2f}")
    else:
        print("tipo de conbustivel invalido")


