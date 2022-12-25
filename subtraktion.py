class Subtraktion:
    minuend: float
    subtrahend: float
    differenz: float

    def input(self):
        minuend_str: str = ""
        print("Bitte gebe den Minuend ein:")
        while True:
            minuend_str = input()
            try:
                self.minuend = float(minuend_str)
                break
            except:
                print("Bitte gebe eine Zahl ein.")
        
        subtrahend_str: str = ""
        print("Bitte gebe den Subtrahend ein:")
        while True:
            subtrahend_str = input()
            try:
                self.subtrahend = float(subtrahend_str)
                break
            except:
                print("Bitte gebe eine Zahl ein.")

    def ergebnis(self):
        self.differenz = self.minuend - self.subtrahend
        print("Die Differenz von "+str(self.minuend)+"-"+str(self.subtrahend)+" ist: "+str(self.differenz))
