class Post:
    def __init__(self, caption, likes):
        self.caption = caption
        self.likes = likes
    
    def get_likes(self):
        return self.likes
    
    def add_like(self):
        self.likes += 1
            
    def display(self):
        print(f'Post caption: {self.caption}')
    
    def __str__(self):
        return f'Post(caption = {self.caption}, likes = {self.likes})'

class Profile:
    def __init__(self, username):
        self.username = username
        self.posts = []
    
    def add_post(self, post):
        self.posts.append(post)

    def display_trending_posts(self):
        for post in self.posts:
            if post.likes >= 10000:
                post.display()

    def __str__(self):
        return f'Profile(username = {self.username})'

post_1 = Post('Photo', 5000)
post_2 = Post('Short video', 6000)

profile_1 = Profile('Mankato State University')

profile_1.add_post(post_1)
profile_1.add_post(post_2)

profile_1.display_trending_posts()
print(profile_1)