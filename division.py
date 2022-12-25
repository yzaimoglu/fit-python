class Division:
    dividend: float
    divisor: float
    quotient: float

    def input(self):
        dividend_str: str = ""
        print("Bitte gebe den Dividend ein:")
        while True:
            dividend_str = input()
            try:
                self.dividend = float(dividend_str)
                break
            except:
                print("Bitte gebe eine Zahl ein.")
        
        divisor_str: str = ""
        print("Bitte gebe den Divisor ein:")
        while True:
            divisor_str = input()
            try:
                self.divisor = float(divisor_str)
                break
            except:
                print("Bitte gebe eine Zahl ein.")

    def ergebnis(self):
        self.quotient = self.dividend / self.divisor
        print("Der Quotient aus "+str(self.dividend)+"/"+str(self.divisor)+" ist: "+str(self.quotient))
