class Hotel:
    def __init__(self, name):
        
        self.name = name
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        
        self.rooms.append(room)

    def get_available_rooms(self, start_date, end_date):
        
        available_rooms = []
        for room in self.rooms:
            if room.is_available(start_date, end_date):
                available_rooms.append(room)
        return available_rooms

    def book_room(self, customer, room_number, start_date, end_date):
        
        room = next((r for r in self.rooms if r.room_number == room_number), None)
        
        if room is None:
            print(f"Room {room_number} does not exist.")
            return
        
        
        if not room.is_available(start_date, end_date):
            print(f"Room {room_number} is not available between {start_date} and {end_date}.")
            return
        
        total_price = room.price * (end_date - start_date)
        
        booking_id = len(self.bookings) + 1
        booking = Booking(booking_id, customer, room, start_date, end_date, total_price)
        
        room.add_booking_dates(start_date, end_date)
        self.bookings.append(booking)
        customer.add_booking(booking)
        
        print(f"Room {room_number} booked successfully for {customer.name} from day {start_date} to day {end_date}.")

class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.booked_dates = []

    def is_available(self, start_date, end_date):
        for booked_start, booked_end in self.booked_dates:
            if not (end_date <= booked_start or start_date >= booked_end):
                return False
        return True

    def add_booking_dates(self, start_date, end_date):
        self.booked_dates.append((start_date, end_date))

class Booking:
    def __init__(self, booking_id, customer, room, start_date, end_date, total_price):
        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = total_price

class Customer:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)


hotel = Hotel("Sunny Hotel")

hotel.add_room(Room(101, "Single", 100))
hotel.add_room(Room(102, "Double", 150))
hotel.add_room(Room(103, "Suite", 200))
name=input("name of the customer: ")
email=input("email-id of the customer: ")
cell=input("Phone Number: ")
if(len(cell) != 10):
    print("Invalid number.Please input again: ")
    cell=input()
customer1 = Customer(name, email,cell)

start_day = input("enter start date: ")
end_day = input("enter end date: ")
start_day=int(start_day)
end_day=int(end_day)
end_day=end_day-start_day+1
start_day=1

available_rooms = hotel.get_available_rooms(start_day, end_day)
print(f"Available rooms from day {start_day} to day {end_day}: {[room.room_number for room in available_rooms]}")
type=input("Please select the room type from: a)single b)double c)suit: ")
room_user=000
if(type== 'single'):
    room_user=101
if(type== 'double'):
    room_user=101
if(type== 'suit'):
    room_user=103
hotel.book_room(customer1, room_user, start_day, end_day)

for booking in customer1.bookings:
    print(f"Booking ID: {booking.booking_id}, Room: {booking.room.room_number}, Total Price: {booking.total_price}")
