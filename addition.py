class Addition:
    erster_summand: float
    zweiter_summand: float
    summe: float

    def input(self):
        erster_summand_str: str = ""
        print("Bitte gebe den ersten Summand ein:")
        while True:
            erster_summand_str = input()
            try:
                self.erster_summand = float(erster_summand_str)
                break
            except:
                print("Bitte gebe eine Zahl ein.")
        
        zweiter_summand_str: str = ""
        print("Bitte gebe den zweiten Summand ein:")
        while True:
            zweiter_summand_str = input()
            try:
                self.zweiter_summand = float(zweiter_summand_str)
                break
            except:
                print("Bitte gebe eine Zahl ein.")

    def ergebnis(self):
        self.summe = self.erster_summand + self.zweiter_summand
        print("Die Summe von "+str(self.erster_summand)+"+"+str(self.zweiter_summand)+" ist: "+str(self.summe))
