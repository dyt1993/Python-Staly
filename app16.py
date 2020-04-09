#磅和公斤转换

weight =int(input("weight: "))
unit = input("(l)bs or (K)g: ): ")

if unit.upper == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")
    