
picachuVida= 100 
picachuAtaque = 30
gigglypuffVida = 100
gigglypuffAtaque = 20
turno = 1
while picachuVida > 0 and gigglypuffVida > 0:
    if turno == 1:
        gigglypuffVida = gigglypuffVida - picachuAtaque
        turno = 0
    if turno == 0:
        picachuVida = picachuVida - gigglypuffAtaque
        turno = 1
print("el gandor fue: ")
if picachuVida > 0:
    print("picachu")
else:
    print("gigglypuff")
