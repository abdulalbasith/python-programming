#Defining a class
# Class names are uppercase
#Allows us to create our own data types
#Every class has to have the "__init__" method. Its alled the constructor. It must accept at least one thing, it has to be 'self'
class Person:
    def __init__(self): #always self
        print ("class instantiated")

    def do_something (self):
        print ("Something done")

#p = Person() #creates an object

#classes are blueprints to create objects 


class Rectangle:
    def __init__ (self, l, w):
        self.length = l #This is how you create properties for a class
        self.width = w
    
    def area (self):
        return self.length * self.width

    def parimeter (self):
        return 2*(self.length + self.width)


r1 = Rectangle (10,5) #Creating an object

print(r1.area())
print (r1.parimeter())

class Playlist:
    def __init__ (self, name):
        self.songs = []
        self.name = name

    # write the add-soung method
    def add_song (self, song):
        #validate the song data
        #has to be a dictionary
        #has to be have title, artist, length

        if type (song) is dict and 'title' in song and 'artist' in song and 'length' in song:
            self.songs.append (song)
        else:
            print ("Error, not a dictionary")
    
    #write get_title Method
    #assume songs are dictionaries

    def get_title (self):
        titles = []
        for song in self.songs:
            titles.append(song['title'])
        return (titles)

    #write the duration method to return the total lenth of the playlist

    def duration(self):
        total_duration = 0
        for song in self.songs:
            total_duration += song['length']
        return total_duration

    


p = Playlist("My_Travel_list")
p.add_song(
    {
    'song':'title',
      'artist' :'Cardi B',
      'length': 3.50
    }
)

p.add_song(
    {'title':'Workout',
      'artist' :'J cole',
      'length': 2.30
    }
)

p.get_title()
p.duration()

