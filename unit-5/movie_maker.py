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
            #print (f"Cast: {self.cast} added to {self.title}")
        else:
            return "Required fields are not supplied"

    def describe(self):
        print (f"Title: {self.title}\nGenre: {self.genre}\nRunning Time: {self.running_time} minutes\nCast: {self.cast}")

    def compare_to (self,other_movie):
        actors_in_common = 0
 
        for actor in self.cast:
            for other_actor in other_movie.cast:
                if actor['name'] == other_actor ['name']:
                    actors_in_common += 1
                    break
            if actors_in_common > 2:
                return -1
        return 1

    def save_to_file(self,filename):

        movie_data = {
        "title":self.title,
        "genre":self.genre,
        "running time":self.running_time,
        "cast":self.cast
        }
        with open(filename,"w") as dump_file:
            json.dump(movie_data,dump_file)
        
