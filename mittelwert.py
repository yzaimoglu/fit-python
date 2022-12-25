from statistics import mean

class Mittelwert:
    zahlen: list
    mittelwert: float

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
        if len(self.zahlen) == 0:
            print("Du hast keine Zahlen eingegeben, deswegen gibt es keinen Mittelwert.")
            return
        self.mittelwert = mean(self.zahlen)
        print("Der Mittelwert der Zahlen ist: "+str(self.mittelwert))
