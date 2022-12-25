class Multiplikation:
    erster_faktor: float
    zweiter_faktor: float
    produkt: float

    def input(self):
        erster_faktor_str: str = ""
        print("Bitte gebe den ersten Faktor ein:")
        while True:
            erster_faktor_str = input()
            try:
                self.erster_faktor = float(erster_faktor_str)
                break
            except:
                print("Bitte gebe eine Zahl ein.")
        
        zweiter_faktor_str: str = ""
        print("Bitte gebe den zweiten Faktor ein:")
        while True:
            zweiter_faktor_str = input()
            try:
                self.zweiter_faktor = float(zweiter_faktor_str)
                break
            except:
                print("Bitte gebe eine Zahl ein.")

    def ergebnis(self):
        self.produkt = self.erster_faktor * self.zweiter_faktor
        print("Die Produkt aus "+str(self.erster_faktor)+"*"+str(self.zweiter_faktor)+" ist: "+str(self.produkt))
