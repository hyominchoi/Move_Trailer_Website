import webbrowser


class Movie(object):
    """ This class stores movie information."""
    
    def __init__ (self):
    	self._title = None
    	self._storyline = None
    	self._poster_image_url = None
    	self._trailer_youtube_url = None

    @property
    def title(self):
    	""" 'title' property """
    	return self._title
     
    @title.setter
    def title(self, value):
    	self._title = value

    @property
    def storyline(self):
    	""" 'storyline' property """
    	return self._storyline
    
    @storyline.setter
    def storyline(self,value):
    	self._storyline = value

    @property
    def poster_image_url(self):
    	""" 'poster_image_url' property """
    	return self._poster_image_url
    
    @poster_image_url.setter
    def poster_image_url(self,value):
    	self._poster_image_url = value

    @property
    def trailer_youtube_url(self):
    	""" 'trailer_youtube_url' property """
    	return self._trailer_youtube_url

    @trailer_youtube_url.setter
    def trailer_youtube_url(self,value):
    	self._trailer_youtube_url = value

    def show_trailer(self):
        webbrowser.open(self._trailer_youtube_url)


