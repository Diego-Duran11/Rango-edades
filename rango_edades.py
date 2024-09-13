RangeAge = int(input("Ingrese Rango de edad: "))

if RangeAge < 0:
    print("pre-infancia")
elif RangeAge >= 0 and RangeAge <= 5:
    print("primera ifancia")
elif RangeAge >=6 and RangeAge <= 11:
    print("infancia")
elif RangeAge >=12 and RangeAge <= 18:
    print("adolescencia")
elif RangeAge >=27 and RangeAge <= 59:
    print("adultez")
elif RangeAge >=60 and RangeAge <= 100:
    print("persona mayor")       
elif RangeAge >=100:
    print("morraquio")