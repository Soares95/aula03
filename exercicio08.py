time1 = (input("digite o primeiro time"))
gtime1 = int (input("Quantos gols o time1 fez?"))

time2 = (input("digite o segundo time"))
gtime2 = int (input("Quantos gols o time2 fez?"))

if gtime2==gtime1:
    print("empatou")
else:
    if gtime1>gtime2:
        print(f"{time1} ganhou! {gtime1}")
    else:
        print(f"{time2} ganhou! {gtime2}")