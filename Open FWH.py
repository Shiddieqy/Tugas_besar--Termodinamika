import CoolProp.CoolProp as CP

h1 = 0
h2 = 0
h3 = 0
h4 = 0
h5 = 0
h6 = 0
h7 = 0
h2s =0
h4s = 0
h6s = 0
h7s = 0

Pb = int(input('masukan P'))
Pu = Pb+2000000
h1 = CP.PropsSI('H', 'P', Pb, 'Q', 0, 'Water')
h7s = CP.PropsSI('H', 'P', Pb, 'Q', 0.98, 'Water')
S7 = CP.PropsSI('S', 'P', Pb, 'Q', 0.98, 'Water')
S1 = CP.PropsSI('S', 'P', Pb, 'Q', 0, 'Water')
y = 0.5


while (True):
    Pu2 = Pu/5
    h2s = CP.PropsSI('H', 'P', Pu2, 'S', S1, 'Water')
    h2 = 1.54*h2s-0.54*h1
    h3 = CP.PropsSI('H', 'P', Pu2, 'Q', 0, 'Water')
    S3 = CP.PropsSI('S', 'P', Pu2, 'Q', 0, 'Water')
    h4s = CP.PropsSI('H', 'P', Pu, 'S', S3, 'Water')
    h4 = 1.54*h4s-0.54*h3
    h6s = CP.PropsSI('H', 'P', Pu2, 'S', S7, 'Water')
    h5 = CP.PropsSI('H', 'P', Pu, 'S', S7, 'Water')
    h7 = 0.9*h7s+0.1*(0.1*h5+0.9*h6s)
    h6 = 0.1*h5+0.9*h6s
    T = CP.PropsSI('T', 'P', Pu , 'H', h5, 'Water')
    y = (h3-h2)/(h6-h2)
    Pu += 10000

    print(Pu,T,((h6-h3)-(1-y)*(h6-h7-h2+h1))/(h5-h4))
    if (((h6-h3)-(1-y)*(h6-h7-h2+h1))/(h5-h4) <= 0.55):
        break

#Kondisi ideal
print("T    H   S   P   X")
print("1", CP.PropsSI('T', 'P', Pb, 'Q', 0, 'Water'), h1, S1, Pb, "0")
print("2", CP.PropsSI('T', 'P', Pu2, 'H', h2s, 'Water'), h2s, CP.PropsSI('S', 'P', Pu2, 'H', h2s, 'Water'), Pu2, "Liquid")
print("3", CP.PropsSI('T', 'P', Pu2, 'H', h3, 'Water'), h3, CP.PropsSI('S', 'P', Pu2, 'H', h3, 'Water'), Pu2, CP.PropsSI('Q', 'P', Pu2, 'H', h3, 'Water'))
print("4", CP.PropsSI('T', 'P', Pu, 'H', h4s, 'Water'), h4s, CP.PropsSI('S', 'P', Pu, 'H', h4s, 'Water'), Pu, CP.PropsSI('Q', 'P', Pu, 'H', h4s, 'Water'))
print("5", T, h5, CP.PropsSI('S', 'P', Pu, 'H', h5, 'Water'), Pu, CP.PropsSI('Q', 'P', Pu, 'H', h5, 'Water'))
print("6", CP.PropsSI('T', 'P', Pu2, 'H', h6s, 'Water'), h6s, CP.PropsSI('S', 'P', Pu2, 'H', h6s, 'Water'), Pu2, CP.PropsSI('Q', 'P', Pu2, 'H', h6s, 'Water'))
print("7", CP.PropsSI('T', 'P', Pb, 'H', h7s, 'Water'), h7s, CP.PropsSI('S', 'P', Pb, 'H', h7s, 'Water'), Pb, CP.PropsSI('Q', 'P', Pb, 'H', h7s, 'Water'))
#Kondisi aktual
print("T    H   S   P   X")
print("1", CP.PropsSI('T', 'P', Pb, 'Q', 0, 'Water'), h1, S1, Pb, "0")
print("2", CP.PropsSI('T', 'P', Pu2, 'H', h2, 'Water'), h2, CP.PropsSI('S', 'P', Pu2, 'H', h2, 'Water'), Pu2, "Liquid")
print("3", CP.PropsSI('T', 'P', Pu2, 'H', h3, 'Water'), h3, CP.PropsSI('S', 'P', Pu2, 'H', h3, 'Water'), Pu2, CP.PropsSI('Q', 'P', Pu2, 'H', h3, 'Water'))
print("4", CP.PropsSI('T', 'P', Pu, 'H', h4, 'Water'), h4, CP.PropsSI('S', 'P', Pu, 'H', h4, 'Water'), Pu, CP.PropsSI('Q', 'P', Pu, 'H', h4, 'Water'))
print("5", T, h5, CP.PropsSI('S', 'P', Pu, 'H', h5, 'Water'), Pu, CP.PropsSI('Q', 'P', Pu, 'H', h5, 'Water'))
print("6", CP.PropsSI('T', 'P', Pu2, 'H', h6, 'Water'), h6, CP.PropsSI('S', 'P', Pu2, 'H', h6, 'Water'), Pu2, CP.PropsSI('Q', 'P', Pu2, 'H', h6, 'Water'))
print("7", CP.PropsSI('T', 'P', Pb, 'H', h7, 'Water'), h7, CP.PropsSI('S', 'P', Pb, 'H', h7, 'Water'), Pb, CP.PropsSI('Q', 'P', Pb, 'H', h7, 'Water'))
print(y)