class Time:
    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins

    def display_time(self):
        print("Time is", self.hours, "hours and", self.mins, "minutes.")

    def display_minute(self):
        print((self.hours * 60) + self.mins)


def add_time():
    time1.hours + time2.hours
    pass


def time_difference(t1, t2):
    pass


time1 = Time(2, 50)
time2 = Time(1, 20)
add_time()
