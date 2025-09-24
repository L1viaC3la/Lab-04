diametri = int(input("Diametri (cm): "))
cmimi_baze = int(input("Çmimi bazë (Lek): "))
if diametri >= 30:
    cmimi_baze += int(cmimi_baze * 0.10)
print("Çmimi final:", cmimi_baze, "Lek")
