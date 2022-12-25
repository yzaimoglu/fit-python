from math import sqrt

class Pythagoras:
    a_sqr: float
    b_sqr: float
    c: float

    def input(self):
        a_sqr_str: str = ""
        print("Bitte gebe a^2 an:")
        while True:
            a_sqr_str = input()
            try:
                self.a_sqr = float(a_sqr_str)
                break
            except:
                print("Bitte gebe eine Zahl ein.")
        
        b_sqr_str: str = ""
        print("Bitte gebe b^2 an:")
        while True:
            b_sqr_str = input()
            try:
                self.b_sqr = float(b_sqr_str)
                break
            except:
                print("Bitte gebe eine Zahl ein.")


    def ergebnis(self):
        self.c = sqrt(self.a_sqr + self.b_sqr)
        print("Bei Nutzung vom Satz des Pythagoras für a^2="+str(self.a_sqr)+" und b^2="+str(self.b_sqr)+" ist die Hypotenuse c: "+str(self.c))
