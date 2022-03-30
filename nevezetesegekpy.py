import nevezetesegekclass
lista=[]
def f1(label):
    print(label)
    x=input("Kérek egy kontinenst: ")
    inputFile("nevezetesegek.txt")
    for i in range(len(lista)):
        if(x == lista[i].kontinens):
            print("\t",lista[i].nev," ",lista[i].varos," ",lista[i].orszag," ",lista[i].kontinens)
       
def f2(label):
    print(label)
    x=input("Kérek egy országot: ")
    inputFile("nevezetesegek.txt")
    for i in range(len(lista)):
        if(x == lista[i].orszag):
            print("\t",lista[i].nev," ",lista[i].varos," ",lista[i].orszag," ",lista[i].kontinens)
        else:
            txt = "\tIlyen nincs a listában"
    print(txt)

def f3(label):
    print(label)
    x=input("Kérek egy országot: ")
    inputFile("nevezetesegek.txt")
    for i in range(len(lista)):
        if(x == lista[i].nev):
            print("\t",lista[i].nev," ",lista[i].varos," ",lista[i].orszag," ",lista[i].kontinens)
        else:
            txt = "\tIlyen nincs a listában"
    print(txt)

def f4(label):
    print(label)
    for i in range(0, 1, 1):
        print("\t", lista[i], " nevezeteség van a listában.")

        



def inputFile(file):
    f=open(file,"r", encoding="utf-8")
    for sor in f:
        sor=sor[0:-1].split(",")
        példány=nevezetesegekclass.Nevezetesegek(sor[0],sor[1],sor[2], sor[3])
        lista.append(példány)
    f.close()


#f1("Kiirom")
#f2("Kiirom")
#f3("Kiirom")
f4("Kiirom")

