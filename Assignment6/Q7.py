class Ticket:
    def __init__(self, movie_name, show_time, seat_number, price):
        self.movie_name = movie_name
        self.show_time = show_time
        self.seat_number = seat_number
        self.price = price

    def display_details(self):
        print("Movie:", self.movie_name)
        print("Show Time:", self.show_time)
        print("Seat Number:", self.seat_number)
        print("Price:", self.price)
        print()

    def get_price(self):
        return self.price


tickets = []
tickets.append(Ticket("Inception", "6:00 PM", "A1", 250))
tickets.append(Ticket("Inception", "6:00 PM", "A2", 250))
tickets.append(Ticket("Inception", "6:00 PM", "A3", 250))

total_amount = 0

for t in tickets:
    t.display_details()
    total_amount += t.get_price()

print("Total Amount to be Paid:", total_amount)
