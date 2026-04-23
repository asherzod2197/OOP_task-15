class TaxiRide:
    def __init__(self, distance, price_per_km):
        self.distance = distance
        self.price_per_km = price_per_km

    def calculate_fare(self):
        total = self.distance * self.price_per_km
        print(f"Yo‘l narxi: {total} so'm")

    def apply_discount(self, percent):
        total = self.distance * self.price_per_km
        discount = total * (1 - percent / 100)
        print(f"Chegirmadan keyin: {int(discount)} so'm")


# Obyekt
ride = TaxiRide(10, 2500)
ride.calculate_fare()
ride.apply_discount(20)
