class TVShow:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
    
    def get_genre(self):
        return self.genre
    
    def set_genre(self, new_genre):
        self.genre = new_genre

    def preview(self):
        print(f'Title: {self.title}, Genre: {self.genre}')

class NetflixDashboard:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.shows = []

    def add_show(self, show):
        self.shows.append(show)
    
    def display_recommendations(self):
        for show in self.shows:
            show.preview()
    
    def __str__(self):
        return f'NetflixDashboard(profile_name = {self.profile_name})'

tvshow_1 = TVShow('The Simpsons', 'comedy')
tvshow_2 = TVShow('King of the Hill', 'comedy')

netflixdashboard_1 = NetflixDashboard('KM login')

netflixdashboard_1.add_show(tvshow_1)
netflixdashboard_1.add_show(tvshow_2)

netflixdashboard_1.display_recommendations()
print(netflixdashboard_1)