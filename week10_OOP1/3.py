# Create a Movie class.
# A Movie has
#  title
#  director
#  runtime minutes

# Create a constructor method that initializes all instance variables.
# You should write getters and setters for each of the instance variables.
# Instantiate an instance of the class. You may pass any initial values of your choosing

class Movie:
    # Constructor
    def __init__(self, title, director, runtime_minutes):
        self.title = title
        self.director = director
        self.runtime_minutes = runtime_minutes
    
    # Getters
    def get_title(self):
        return self.title
    def get_director(self):
        return self.director
    def get_runtime_minutes(self):
        return self.runtime_minutes
    
    # Setters
    def set_title(self, new_title):
        self.title = new_title
    def set_director(self, new_director):
        self.director = new_director
    def set_runtime_minutes(self, new_runtime_minutes):
        self.runtime_minutes = new_runtime_minutes

movie1 = Movie('Titanic', 'James Cameron', 195)

print(movie1.get_title())
print(movie1.get_director())
print(movie1.get_runtime_minutes())

print(f'Title of movie: {movie1.get_title()}')
print(f'Director: {movie1.get_director()}')
print(f'Runtime of movie: {movie1.get_runtime_minutes()} minutes')
