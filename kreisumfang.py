from math import pi

class Kreisumfang:
    radius: float
    umfang: float

    def input(self):
        radius_str: str = ""
        print("Bitte gebe den Radius des Kreises an:")
        while True:
            radius_str = input()
            try:
                self.radius = float(radius_str)
                break
            except:
                print("Bitte gebe eine Zahl ein.")

    def ergebnis(self):
        self.umfang = self.radius * 2 * pi
        print("Der Umfang eines Kreises mit dem Radius "+str(self.radius)+" ist: "+str(self.umfang))
