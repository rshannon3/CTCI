"""
7 .3 Jukebox: Design a musical jukebox using object oriented principles.
Hints:#798
"""
import random

class Song:
	def __init__(self, title=None, artist=None, album=None):
		self.title = title
		self.artist = artist
		self.album = album


class Jukebox:
	VOLUME_DEFAULT = 50
	def __init__(self, songs=None):
		self.song_list = songs
		self.volume = VOLUME_DEFAULT
		self.current_song = None

	def select_song(self, title):
		for song in self.song_list:
			if title == song.title:
				self.current_song = song
				break

	def play(self):
		pass

	def pause(self):
		pass

	def volume_up(self, up):
		self.volume = min(100, self.volume + up)

	def volume down(self, down):
		self.volume = max(0, self.volume - down)

	def shuffle(self):
		select_song( self.song_list[ random.randint(0,len(self.song_list)) ].title )
