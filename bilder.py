from PIL import Image
import time


def pixelsausgeben():
    img = Image.open(
        "C:/Users/LeoVogel/Desktop/Programmieren/Random/frame.jpg")
    hello = 0
    pixels = img.load()
    print("Anzahl Pixel: " + str(img.width*img.height)
          )
    time.sleep(3)
    for i in range(img.width):
        for j in range(img.height):
            hello += 1

            print(hello)
            print(pixels[i, j])


def pixelchange(eingabe):
    img = Image.open(
        "C:/Users/LeoVogel/Desktop/Programmieren/Random/frame.jpg"
    )
    pixels = img.load()

    res = ''.join(format(ord(i), 'b') for i in eingabe)
    i = 0
    j = 0

    print(res)
    while (i < len(res)):
        between = pixels[0, i]
        neuerwert = between[2] - 1
        if (res[j] == "1"):

            pixels[0, i] = (between[0], between[1], neuerwert)
            print("0, " + str(i) + " wird von" +
                  str(between) + " zu " + str(pixels[0, i]))
        else:

            print("Zero: 0, " + str(i)
                  + " wird von" + str(between) + " zu " + str(pixels[0, i]))
        i += 1
        j += 1

    between = pixels[0, i]
    neuerwert = between[2] - 2
    pixels[0, i] = (between[0], between[1], neuerwert)
    print("Der letzte Pixel ist: " + str(pixels[0, i]))
    print(eingabe + " wurde im Bild versteckt")
    img.save("C:/Users/LeoVogel/Desktop/Programmieren/Random/frame2.jpg")
    img = Image.open(
        "C:/Users/LeoVogel/Desktop/Programmieren/Random/frame2.jpg"
    )
    pixels = img.load()
    print(pixels[0, 0])
    print(pixels[0, 1])
    print(pixels[0, 2])
    print(pixels[0, 3])
    print(pixels[0, 4])
    print(pixels[0, 5])


def Auswertung():

    i = 0
    ergebnis = ""
    j = True

    while (j):
        img = Image.open(
            "C:/Users/LeoVogel/Desktop/Programmieren/Random/frame2.jpg"
        )
        pixels = img.load()
        print(pixels[0, i][2])
        wert1 = pixels[0, i][2]

        img2 = Image.open(
            "C:/Users/LeoVogel/Desktop/Programmieren/Random/frame - Kopie.jpg"
        )
        pixels2 = img2.load()
        print(pixels2[0, i][2])
        wert2 = pixels2[0, i][2]

        if (((wert1) - (wert2)) == 0):
            ergebnis += "0"
            print(ergebnis)
        elif (((wert1) - (wert2)) == 1):
            ergebnis += "1"
            print(ergebnis)
        elif (((wert1) - (wert2)) == 2):
            j = True
        i += 1


pixelchange("8")

Auswertung()
