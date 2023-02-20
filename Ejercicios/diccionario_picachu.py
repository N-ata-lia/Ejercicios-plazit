def run ():
    picachu = {
        "vida": 100,
        "ataque": 30,
    }

    gigglypuff = {
        "vida": 100,
        "ataque": 20,
    }



    turno = 1
    while picachu["vida"] > 100 and  gigglypuff["vida"] > 100:
        if turno == 1:
            gigglypuff["vida"] = gigglypuff["vida"] -picachu["ataque"] 
            turno = 0
        if turno == 0:
            picachu["vida"] = picachu["vida"] - gigglypuff["ataque"]
            turno = 1
    print("el gandor fue: ")
    if picachu["vida"] > 100:
        print("picachu")
    else:
        print("gigglypuff")

if __name__ == "__main__":
    run()