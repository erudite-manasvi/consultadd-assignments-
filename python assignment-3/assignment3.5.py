# Create a class 'Time' and initialize it with hours and minutes. Create a method addTime() which should take two Time objects and add them.
class Time:
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes

    def sum(self, t1, t2):
        total_minutes = t1.minutes + t2.minutes
        self.hours = total_minutes // 60
        self.minutes = total_minutes % 60
        self.hours += t1.hours + t2.hours

    def display_time(self):
        print(f"{self.hours} hours and {self.minutes} minutes")
    
t1 = Time(2,45)
t2 = Time(4,30)
t = Time(0,0)

t.sum(t1,t2)
t.display_time()