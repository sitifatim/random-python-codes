import datetime as dt

hari = dt.date.today()
print(hari)

dulu = dt.date(2000,10,17)
print(dulu)
print(f"hari waktu itu: {dulu:%A}")