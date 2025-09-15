from address import Address
from mailing import Mailing

to_address = Address("422110","Кукмор","Гафиятуллина","1","21")
from_address = Address("420098","Казань","Лукина","40","53")

mail = Mailing(to_address,from_address,350,"ABC123")

print(
      f"Отправление{mail.track}из{mail.from_address.index},{mail.from_address.city},"
      f"{mail.from_address.street},{mail.from_address.house}-{mail.from_address.apartment}"
      f"в{mail.to_address.index},{mail.to_address.city},{mail.to_address.street},"
      f"{mail.to_address.house}-{mail.to_address.apartment}.Стоимость{mail.cost}рублей"
)