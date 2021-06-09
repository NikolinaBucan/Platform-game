print("Unesi vreme na Aljasci:")
x = input()
print("Unesi am ili pm")
z = input()
if z=="am":
    x=x
if z=="pm":
    x=int(x)+12
y=int(x)+10
if y<12:
    print("Vreme u Srbiji:" + str(y) + "am")
elif y==12 :f
    print("Vreme u Srbiji:" +str(y) + "pm")
elif y== 34 and z == "pm":
    y=y-24
    print("Vreme u Srbiji:" + str(y) + "pm")
elif y== 22 and z == "am":
    y = y - 12
    print("Vreme u Srbiji:" + str(y) + "am")
elif 12<y<24 and not y==22:
    y=y-12
    print("Vreme u Srbiji:" + str(y) + "pm")
elif y==24:
    y=int(y/2)
    print("Vreme u Srbiji:" + str(y) + "am")
elif y>24:
    y=y-24
    print("Vreme u Srbiji:" + str(y) + "am")
else:
    print("Niste uneli dobre vrednosti")
