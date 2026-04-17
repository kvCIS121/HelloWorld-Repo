class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def __add__(self, other_times):
        new_hours = self.hours + other_times.hours
        new_minutes = self.minutes + other_times.minutes

        # Normalize minutes (e.g., 75 minutes → 1 hour 15 minutes)
        if new_minutes >= 60:
            new_hours += new_minutes // 60
            new_minutes += new_minutes % 60
        
        return Time(new_hours, new_minutes)
       
    
    def __str__(self):
        return f'Time (hours = {self.hours}, minutes = {self.minutes})'
    
t_1 = Time(1,30)
t_2 = Time(2,45)
t_3 = t_1 + t_2

# Print readable format
print('t_1: ', t_1)
print('t_2: ', t_2)
print('t_3: ', t_3)

print(t_3)