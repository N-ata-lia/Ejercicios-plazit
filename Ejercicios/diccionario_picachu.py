def run ():
    picachu = {
        "vida" = 100,
        "ataque" = 30,
    }

    gigglypuff ={
        "vida" = 100,
        "ataque" = 20,
    }

        turno = 1
    while picachu Vida > 0 and gigglypuff Vida > 0:
        if turno == 1:
            gigglypuff  Vida = gigglypuff Vida - picachu Ataque
            turno = 0
        if turno == 0:
            picachu Vida = picachu Vida - gigglypuff Ataque
            turno = 1
    print("el gandor fue: ")
    if picachu Vida > 0:
        print("picachu")
    else:
        print("gigglypuff")

if __name__ == "__main__":
    run()