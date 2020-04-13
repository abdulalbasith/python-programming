import movie_maker as m

movie1 = m.Movie("Movie 1","Thriller",120)
movie1.add_cast({"name":"Blinder", "age":32, "sex":"M"})
movie1.add_cast({"name":"Jessica","age":33,"sex":"F"})
movie1.add_cast({"name":"Donny", "age":37, "sex":"M"})
movie1.add_cast({"name":"Anne","age":38,"sex":"F"})

movie2 = m.Movie("Movie 2","Thriller",120,[{"name":"Blinder", "age":32, "sex":"M"},{"name":"Anne","age":38,"sex":"F"},{"name":"Danny", "age":33, "sex":"M"},{"name":"Donny","age":37,"sex":"M"},{"name":"Jessica","age":38,"sex":"F"}])

'''
movie2.add_cast({"name":"Blinder", "age":32, "sex":"M"})
movie2.add_cast({"name":"Anne","age":38,"sex":"F"})
movie2.add_cast({"name":"Danny", "age":33, "sex":"M"})
'''
#movie1.describe()
#movie2.describe()

movie2.save_to_file()
