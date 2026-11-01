#Problem 9: Electricity Bill with Progressive Tiers
def electricity_bill(kwh):
    if kwh < 0:
        return None
    tier1 = min(kwh, 50)                 # first 50 kWh
    tier2 = min(max(kwh - 50, 0), 150)   # next 150 kWh
    tier3 = max(kwh - 200, 0)            # everything above 200 kWh
    total = tier1 * 480 + tier2 * 610 + tier3 * 730 + 2000
    return round(total * 1.10)           # add 10% VAT


#(b) Table
for kwh in [0, 35, 50, 120, 200, 350]:
    bill = electricity_bill(kwh)
    usd = bill / 4100
    print(f"{kwh:>3} kWh -> {bill:>8,} riel (= {usd:>5.2f} USD)")

#(c) Ask the user
kwh = float(input("\nEnter your monthly consumption (kWh): "))
bill = electricity_bill(kwh)
if bill is None:
    print("Invalid input: consumption cannot be negative.")
else:
    print(f"Your bill is {bill:,} riel (= {bill / 4100:.2f} USD)")