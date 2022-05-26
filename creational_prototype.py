#                               Example for <prototype> pattern Design
#                          ************************************************
class Cinema:
    pass


class Movie:
    pass


class Time:
    pass


class Hall:
    def __init__(self, capacity):
        self.capacity = capacity


class Seat:
    def __init__(self, number):
        self.number = number


class Sens:
    def __init__(self, cinema, movie, time, hall):
        self.cinema = cinema
        self.movie = movie
        self.time = time
        self.hall = hall
        self.seats = list()
        self.prototype_seats()

    def prototype_seats(self):
        for i in range(self.hall.capacity):
            self.seats.append(Seat(i))


movie = Movie()
cinema = Cinema()
time = Time()
hall = Hall(110)

sens = Sens(cinema, movie, time, hall)
print(len(sens.seats))
print(type(sens.seats[0]))
