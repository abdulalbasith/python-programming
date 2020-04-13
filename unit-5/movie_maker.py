import json
class Movie:
    def __init__(self, title ="", genre="", running_time=0, cast = []):
        self.title = title
        self.genre = genre
        self.running_time = running_time
        self.cast = cast
   
    def add_cast (self, cast_to_add = {}):
        if "name" in cast_to_add and "age" in cast_to_add and "sex" in cast_to_add:
            self.cast.append(cast_to_add)
            print (f"Cast: {self.cast} added to {self.title}")
        else:
            return "Required fields are not supplied"

    def describe(self):
        print (f"Title: {self.title}\nGenre: {self.genre}\nRunning Time: {self.running_time} minutes\nCast: {self.cast}")

    def compare_to (self,Movie):
        actors_in_common = 0
        for actor in self.cast:
            if self.cast[actor] == Movie.cast[actor]:
                actors_in_common += 1
            if actors_in_common < 2:
                return -1
            else:
                return 1

    def save_to_file(self,filename):

        movie_data = {
        "title":self.title,
        "genre":self.genre,
        "running time":self.running_time,
        "cast":self.cast
        }
        f = open(filename,"w+")
        f.write(json.dumps(movie_data))
        f.close()

        
movie1 = Movie("Movie 1","Thriller",120)
movie1.add_cast({"name":"Blinder", "age":32, "sex":"M"})
movie1.add_cast({"name":"Jessica","age":33,"sex":"F"})
movie1.add_cast({"name":"Donny", "age":37, "sex":"M"})

movie2 = Movie("Movie 2","Thriller",120,[{"name":"Blinder", "age":32, "sex":"M"},{"name":"Anne","age":38,"sex":"F"},{"name":"Danny", "age":33, "sex":"M"}])

