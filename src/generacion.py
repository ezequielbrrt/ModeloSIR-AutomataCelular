def escribirConteo(auxestados):
    global sano,s,inf,r
    for it in auxestados:
        if it == "0":
            sano += 1
        if it == "1":
            s += 1
        if it == "2":
            inf += 1
        if it == "3":
            r += 1
    grafica = open("GraficaSano.txt","a")
    grafica.write(str(sano)+","+str(tiempo)+"\n")
    grafica = open("GraficaS.txt","a")
    grafica.write(str(s)+","+str(tiempo)+"\n")
    grafica = open("GraficaI.txt","a")
    grafica.write(str(inf)+","+str(tiempo)+"\n")
    grafica = open("GraficaR.txt","a")
    grafica.write(str(r)+","+str(tiempo)+"\n")