from smartphone import Smartphone

catalog = [
Smartphone("Apple","iPhone 14","+79172345678"),
Smartphone("Samsung","Galaxy S40","+79127354379"),
Smartphone("Xiaomi","Redmi Note 13","+79053677358"),
Smartphone("Google","Pixel 6","+79156385279"),
Smartphone("OnePlus","11 Pro","+79273660487")]

for phone in catalog:
 print(f"{phone.brand}-{phone.model}.{phone.number}")

