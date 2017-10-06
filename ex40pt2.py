class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

Time_to_die = Song(["U are going to die", "I'm sorry i don't like to lie", "There is nothing that you can try"])

die_in_the_sky = Song(["The sky is where your going to die", "So you might as well cry"])

Why_die_so_high = Song(["The sky is falling so your better run", "There is no place to hide or no place to die.", "Isnt this song amazing."])


Time_to_die.sing_me_a_song()

die_in_the_sky.sing_me_a_song()

Why_die_so_high.sing_me_a_song()
