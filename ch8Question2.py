def tempConverter(degree):
    farenheit = (1.8*degree) + 32
    return farenheit
deg = int(input("degree pls: "))
print(f"farenheit is {tempConverter(deg)}")