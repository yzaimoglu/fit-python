from rechenart import Rechenart
from colors import ansi_colors
from addition import Addition
from subtraktion import Subtraktion
from division import Division
from multiplikation import Multiplikation
from mittelwert import Mittelwert
from maximum import Maximum
from minimum import Minimum
from kreisumfang import Kreisumfang
from pythagoras import Pythagoras

while True:
    print("")
    print("")
    print(ansi_colors.BOLD+ansi_colors.OKBLUE+"Willkommen bei dem Taschenrechner."+ansi_colors.ENDC)
    print(ansi_colors.OKBLUE+"Bitte gebe deine gewünschte Rechenart aus der folgenden Liste mit der entsprechenden Zahl an:"+ansi_colors.ENDC)
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Division")
    print("4. Multiplikation")
    print("5. Mittelwert")
    print("6. Summe einer Liste")
    print("7. Maximum einer Liste")
    print("8. Minimum einer Liste")
    print("9. Umfang eines Kreises")
    print("10. Satz des Pythagoras")
    print(ansi_colors.FAIL+"Gebe \"ende\" ein um das Programm zu beenden."+ansi_colors.ENDC)
    print("")

    rechenart_string: str = input()
    rechenart_int: Rechenart = Rechenart.NULL;

    try:
        rechenart_int = Rechenart(int(rechenart_string))
        match rechenart_int:
            case Rechenart.ADDITION:
                addition = Addition()
                addition.input()
                addition.ergebnis()
            case Rechenart.SUBTRAKTION:
                subtraktion = Subtraktion()
                subtraktion.input()
                subtraktion.ergebnis()
            case Rechenart.DIVISION:
                division = Division()
                division.input()
                division.ergebnis()
            case Rechenart.MULTIPLIKATION:
                multiplikation = Multiplikation()
                multiplikation.input()
                multiplikation.ergebnis()
            case Rechenart.LISTE_MITTELWERT:
                mittelwert = Mittelwert()
                mittelwert.input()
                mittelwert.ergebnis()
            case Rechenart.LISTE_MAXIMUM:
                maximum = Maximum()
                maximum.input()
                maximum.ergebnis()
            case Rechenart.LISTE_MINIMUM:
                minimum = Minimum()
                minimum.input()
                minimum.ergebnis()
            case Rechenart.KREISUMFANG:
                kreisumfang = Kreisumfang()
                kreisumfang.input()
                kreisumfang.ergebnis()
            case Rechenart.PYTHAGORAS:
                pythagoras = Pythagoras()
                pythagoras.input()
                pythagoras.ergebnis()
    except:
        if rechenart_string.lower() == "ende" or rechenart_string.lower() == "exit":
            break
        else:
            print("Bitte gebe eine richtige Zahl ein.")
