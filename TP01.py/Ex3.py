# Problem 3: Temperature Converter
def celsius_to_fahrenheit(c, round_to=1):
    f = c * 9 / 5 + 32
    return round(f, round_to)


def fahrenheit_to_celsius(f, round_to=1):
    c = (f - 32) * 5 / 9
    return round(c, round_to)


# (a) Conversion table
print("  °C  |   °F")
print("-" * 6 + "+" + "-" * 7)
for c in range(0, 101, 20):
    print(f"{c:>5} | {celsius_to_fahrenheit(c):>6}")

# (b) Normal body temperature in Celsius
print(f"98.6 °F = {fahrenheit_to_celsius(98.6)} °C")

# (c) Round trip: 37 °C -> °F -> °C
f = celsius_to_fahrenheit(37)
back = fahrenheit_to_celsius(f)
# print(f"37 °C = {f} °F; back again = {back} °C")

# (d) Using a non-default round_to
# print(fahrenheit_to_celsius(100, round_to=3))