class Signal:

    
    def __init__(self, ship, planet, coord_place, direction):
        self.shipcode: str = ship[0]
        self.shipnumber: str = ship[1]
        self.planet: str = planet
        self.coordplaceX: int = int(coord_place[0])
        self.coordplaceY: int = int(coord_place[1])
        self.directionX: int = int(direction[0])
        self.directionY: int = int(direction[1])
        self.shipname: str = f"{ship[0]}-{ship[1]}"

    def __str__(self) -> str:
        return f"{self.shipcode}-{self.shipnumber} {self.planet} {self.coordplaceX} {self.coordplaceY} {self.directionX} {self.directionY}"

def coord_fix(x, y, n, m, t, xd, yd):
    if n <= 5:
        x = -(n + xd) * 4 + t
    if n > 5:
        x = n + xd
    if m > 3:
        y = m + t + yd
    if m <= 3:
        y = -(n + yd) * m
    return [x, y]

with open('space.txt', encoding='utf-8') as f:
    raw = f.readlines()

rawsignals = []
signals: list[Signal] = []

fixedsignals = []
fixedsignalsoutput = []
validsignals = []

for el in raw:
    el = el.replace("\n", "")
    rawsignals.append(el.split("*"))

for signal in rawsignals:
    signals.append(Signal(signal[0].split("-"), signal[1], signal[2].split(), signal[3].split()))

for signal in signals:
    shipname = f"{signal.shipcode}-{signal.shipnumber}"
    x = signal.coordplaceX
    y = signal.coordplaceY
    n = int(signal.shipnumber[0])
    m = int(signal.shipnumber[1])
    t = len(signal.planet.replace(" ", ""))
    xd = signal.directionX
    yd = signal.directionY
    fixedcoord = coord_fix(x, y, n, m, t, xd, yd)

    fixedsignalsoutput.append(f"{shipname} - {fixedcoord[0], fixedcoord[1]}\n")


    if signal.shipcode[-1] == "V":
        validsignals.append(f"{shipname} - {fixedcoord[0], fixedcoord[1]}\n")

def coord_fix(x, y, n, m, t, xd, yd):
    if n <= 5:
        x = -(n + xd) * 4 + t
    if n > 5:
        x = n + xd
    if m > 3:
        y = m + t + yd
    if m <= 3:
        y = -(n + yd) * m
    return [x, y]
    
def task1():
    with open("space_new.txt", 'a', encoding='utf-8') as f:
        f.writelines(fixedsignalsoutput)

    for i in validsignals:
        print(i)

def task3():
    inp = input()
    while inp != "stop":
        for signal in signals:
            if inp == signal.shipname:
                print(f"Корабль {signal.shipname} был отправлен с планеты: {signal.planet} и его направление движения было: {signal.directionX} {signal.directionY}")
                break
        inp = input()

def generate_password(planet, shipcode):
    return f"{planet[-3:]}{shipcode[2]}{shipcode[1]}{planet[2]}{planet[1]}{planet[0]}".upper()


def task4():
    with open("space_uniq_password.csv", 'a', encoding='utf-8') as f:
        f.write(f"ShipName;planet;password\n")
    with open("space_uniq_password.csv", 'a', encoding='utf-8') as f:
        for signal in signals:
            planet = signal.planet
            shipcode = signal.shipcode
            
            f.write(f"{signal.shipname};{signal.planet};{generate_password(planet, shipcode)}\n")
        
