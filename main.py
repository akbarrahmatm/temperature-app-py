print ("Program Konversi Suhu\n")
print ("\n1. Dari Celcius", "\n2. Dari Reamur", "\n3. Dari Fahrenheit", "\n4. Dari Kelvin")

satuan = int(input("Masukkan satuan suhu awal : "))

if satuan == 1:
    # celcius

    celcius = float(input("Masukkan suhu dalam celcius : "))

    # reamur

    reamur = ((4/5) * celcius)

    # fahrenheit

    fahrenheit = ((9/5) * celcius) + 32

    # kelvin

    kelvin = celcius + 273

    # hasil
    print("\n Reamur :", reamur, "R \n", "Fahrenheit :", fahrenheit, "F \n", "Kelvin :", kelvin, "K \n")
elif satuan == 2:

    # reamur

    reamur = float(input("Masukkan suhu dalam reamur : "))

    # celcius

    celcius = (5/4) * reamur

    # fahrenheit

    fahrenheit = ((9/4) * reamur) + 32

    # kelvin

    kelvin = ((5/4) * reamur) + 273

    # hasil
    print("\n Celcius :", celcius, "C \n", "Fahrenheit :", fahrenheit, "F \n", "Kelvin :", kelvin, "K \n")

elif satuan == 3:

    # fahrenheit

    fahrenheit = float(input("Masukkan suhu dalam fahrenheit : "))

    # celcius

    celcius = 5/9 * (fahrenheit - 32)

    # reamur

    reamur = 4/9 * (fahrenheit - 32)

    # kelvin

    kelvin = (5/9 * (fahrenheit - 32)) + 273

    # hasil
    print("\n Celcius :", celcius, "C \n", "Reamur :", reamur, "R \n", "Kelvin :", kelvin, "K \n")

elif satuan == 4:
    # kelvin

    kelvin = float(input("Masukkan suhu dalam kelvin : "))

    # celcius

    celcius = kelvin - 273

    # reamur

    reamur = 4/5 * (kelvin - 273)

    # fahrenheit

    fahrenheit = (9/5 * (kelvin - 273)) + 32

    # hasil
    print("\n Celcius :", celcius, "C \n", "Reamur :", reamur, "R \n", "Fahrenheit :", fahrenheit, "F \n")

else:
    print("Parameter yang anda masukkan tidak benar")