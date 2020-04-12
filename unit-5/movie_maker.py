class Movie:
    def __init__(self, title ="", genre="", running_time=0, casts = []):
        self.title = title
        self.genre = genre
        self.running_time = running_time
        self.casts = casts 
        print (f'The movie, "{title}" is created')
    
    def add_cast (self, cast={}):
        if "name" in cast and "age" in cast and "sex" in cast:
            self.casts.append(cast)
        else:
            return "Required fields are not supplied"

    def describe(self):
        print (f"Title: {self.title}\nGenre: {self.genre}\nRunning Time: {self.running_time} minutes\nCast: {self.casts}")

    def compare_to (self,Movie):
        for actor in self.casts:

movie1 = Movie("")