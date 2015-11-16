import fresh_tomatoes
import media

# This file stores movie list in media class format :
# title, storyline(imdb link), poster_url, youtube_url
# class instance name is from its title in lower_cases

erin_brockovich = media.Movie()
erin_brockovich.title = "Erin Brockovich"
erin_brockovich.storyline = "http://www.imdb.com/title/tt0195685/"
erin_brockovich.poster_image_url = "http://www.gstatic.com/tv/thumb/movieposters/24917/p24917_p_v7_aa.jpg"
erin_brockovich.trailer_youtube_url = "www.youtube.com/watch?v=9TjEklyF7-E"

hotel_rwanda = media.Movie()
hotel_rwanda.title = "Hotel Rwanda"
hotel_rwanda.storyline = "http://www.imdb.com/title/tt0395169/?ref_=fn_al_tt_1"
hotel_rwanda.poster_image_url = "http://www.gstatic.com/tv/thumb/movieposters/35240/p35240_p_v7_aa.jpg"
hotel_rwanda.trailer_youtube_url = "www.youtube.com/watch?v=qZzfxL90100"

camille_claudel = media.Movie()
camille_claudel.title = "Camille Claudel"
camille_claudel.storyline = "http://www.imdb.com/title/tt2018086/?ref_=fn_al_tt_2"
camille_claudel.poster_image_url =  "https://upload.wikimedia.org/wikipedia/en/f/f6/Camille_Claudel_1915_poster.jpg"
camille_claudel.trailer_youtube_url = "https://youtu.be/UsB9QoMgr0I"

huit_femmes = media.Movie()
huit_femmes.title = "8 Femmes"
huit_femmes.storyline = "http://www.imdb.com/title/tt0283832/?ref_=fn_al_tt_1"
huit_femmes.poster_image_url = "https://upload.wikimedia.org/wikipedia/en/2/22/8-femmes-poster.jpg"
huit_femmes.trailer_youtube_url = "www.youtube.com/watch?v=CAxqXsao2Ew"

# movies is a list of movies from above
movies = [erin_brockovich, hotel_rwanda, camille_claudel, huit_femmes]

# this will create html page
fresh_tomatoes.open_movies_page(movies)
