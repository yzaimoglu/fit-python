class SummeListe:
    zahlen: list
    summe: float

    def input(self):
        self.zahlen = []
        input_str: str = ""
        print("")
        print("Du kannst so viele Zahlen eingeben wie du willst. Bitte gebe diese einzeln an.")
        print("Sobald du fertig bist kannst du \"fertig\" schreiben.")
        while True:
            input_str = input()
            try:
                input_float: float = float(input_str)
                self.zahlen.append(input_float)
            except:
                if input_str.lower() == "fertig" or input_str.lower() == "ende" or input_str.lower() == "exit":
                    break
                else:
                    print("Bitte gebe eine Zahl ein oder schreibe \"fertig\" wenn du fertig bist.")

    def ergebnis(self):
        self.summe = 0
        for zahl in self.zahlen:
            self.summe += zahl
        print("Die Summe der Zahlen ist: "+str(self.summe))

