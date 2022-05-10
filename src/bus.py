class Bus:
    def __init__(self, number, destination):
        self.route_number = number
        self.destination = destination
        self.passengers = []
    
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, passenger):
        self.passengers.append(passenger)
    
    def drop_off(self, passenger):
        self.passengers.remove(passenger)
    
    def empty(self):
        self.passengers = []
    
    def pick_up_from_stop(self, bus_stop):
        passengers = bus_stop.queue
        for passenger in passengers:
            self.pick_up(passenger)
        
        bus_stop.clear
