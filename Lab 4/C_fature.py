cmimi = float(input("Cmimi (Lek): "))
sasia = int(input("Sasia (copë): "))

if sasia < 0:
    print("Sasia e pavlefshme")
else:
    karta = input("Ke kartë studenti? (po/jo): ")
    nentotal = cmimi * sasia
    zbritje = 0
    if karta.lower() == "po":
        zbritje = nentotal * 0.10
    tvsh = (nentotal - zbritje) * 0.15
    total = nentotal - zbritje + tvsh

    print("------------------------------")
    print("Nën-total:", round(nentotal, 2), "Lek")
    print("Zbritja: 10% (Vlera:", round(zbritje, 2), "Lek)")
    print("TVSH (15%):", round(tvsh, 2), "Lek")
    print("Totali për pagesë:", round(total, 2), "Lek")
