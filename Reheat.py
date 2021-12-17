import CoolProp.CoolProp as CP

h1 = 0
h2 = 0
h3 = 0
h4 = 0
h5 = 0
h6 = 0
h4s = 0
h6s = 0

Pb = int(input('masukan P'))
Pu = Pb+2000000
h1 = CP.PropsSI('H', 'P', Pb, 'Q', 0, 'Water')
h6s = CP.PropsSI('H', 'P', Pb, 'Q', 0.95, 'Water')
S1 = CP.PropsSI('S', 'P', Pb, 'Q', 0, 'Water')



while (True):
    Pu2 = Pu - 500000
    S6 = CP.PropsSI('S', 'P', Pb, 'Q', 0.95, 'Water')
    h5 = CP.PropsSI('H', 'P', Pu2 , 'S', S6, 'Water')
    h6 = 0.9*h6s+0.1*h5
    h2s = CP.PropsSI('H', 'P', Pu, 'S', S1, 'Water')
    h2 = 1.54*h2s-0.54*h1
    T = CP.PropsSI('T', 'P', Pu2 , 'S', S6, 'Water')
    h3 = CP.PropsSI('H', 'T', T, 'P', Pu, 'Water')
    S3 = CP.PropsSI('S', 'T', T, 'P', Pu, 'Water')
    h4s = CP.PropsSI('H', 'S', S3, 'P', Pu2, 'Water')
    h4 = 0.9*h4s+0.1*h3
    Pu += 1000
    print(Pu,T,(h6-h1)/(h3+h5-h2-h4))
    if ((h6-h1)/(h3+h5-h2-h4) <= 0.55):
        break

print(Pu)
