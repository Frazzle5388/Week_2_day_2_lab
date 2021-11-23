class Bus:
    def __init__(self, route_number,destination, price, capacity):
        self.route_number = route_number
        self.destination = destination
        self.price = price
        self.capacity = capacity
        self.passengers = []
        self.till = 0

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)

    def remaining_capacity(self):
        return self.capacity - passengers_on_bus()

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self,person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers = []

    def fare(self,person):
        person.cash -= self.price
        self.till += self.price

    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            self.pick_up(passenger)


