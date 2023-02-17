def run ():
    picachu = {
        "Vida": 100,
        "Ataque": 30,
    }

    gigglypuff ={
        "Vida": 100,
        "Ataque": 20,
    }

    turno = 1
    while Vida > 0 and Vida > 0:
        if turno == 1:
            Vida = Vida - Ataque
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