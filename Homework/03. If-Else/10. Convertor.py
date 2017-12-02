chislozapreobrazuvane = float(input())
vhodnamernaedenica = str(input())
izhodnamernaedenica = str(input())

if vhodnamernaedenica == "m":
    edenicavmetri = chislozapreobrazuvane
elif vhodnamernaedenica == "mm":
    edenicavmetri = chislozapreobrazuvane / 1000
elif vhodnamernaedenica == "cm":
    edenicavmetri = chislozapreobrazuvane / 100
elif vhodnamernaedenica == 'mi':
    edenicavmetri = chislozapreobrazuvane / 0.000621371192
elif vhodnamernaedenica == "in":
    edenicavmetri = chislozapreobrazuvane / 39.3700787
elif vhodnamernaedenica == "km":
    edenicavmetri = chislozapreobrazuvane * 1000
elif vhodnamernaedenica == 'ft':
    edenicavmetri = chislozapreobrazuvane / 3.2808399
elif vhodnamernaedenica == 'yd':
    edenicavmetri = chislozapreobrazuvane / 1.0936133

if izhodnamernaedenica == "m":
    print(str(edenicavmetri) + ' m')
elif izhodnamernaedenica == "mm":
    print(str(edenicavmetri * 1000) + ' mm')
elif izhodnamernaedenica == 'cm':
    print(str(edenicavmetri * 100) + ' cm')
elif izhodnamernaedenica == 'mi':
    print(str(edenicavmetri * 0.000621371192) + ' mi')
elif izhodnamernaedenica == 'in':
    print(str(edenicavmetri * 39.3700787) + ' in')
elif izhodnamernaedenica == 'km':
    print(str(edenicavmetri / 1000) + ' km')
elif izhodnamernaedenica == 'ft':
    print(str(edenicavmetri * 3.2808399) + ' ft')
elif izhodnamernaedenica == 'yd':
    print(str(edenicavmetri * 1.0936133) + ' yd')