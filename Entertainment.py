import fresh_tomatoes
import media

#toystory=media.Movie("Toy Story","A story of a boy and his toys that came to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=4KPTXpQehio")
#print(toystory.storyline)

#avatar=media.Movie("Avatar","A marine on an alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print(avatar.storyline)
#avatar.show_trailer()

ratatoullie=media.Movie("Ratatoullie","A story of a Rat and his love for cooking","https://54disneyreviews.files.wordpress.com/2015/07/ratatouille1.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")

transformers=media.Movie("Transformers","Autobots and the Decepticons","https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",
                        "https://www.youtube.com/watch?v=dxQxgAfNzyE")

#print(ratatoullie.storyline)
#ratatoullie.show_trailer()

#school_of_rock=media.Movie("School of Rock","Using rock music to learn","https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=3PsUJFEBC74")

#midnight_in_paris=media.Movie("Midnight in Paris","Going back in time to meet authors","https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg","https://www.youtube.com/watch?v=FAfR8omt-CY")

#hunger_games=media.Movie("The Hunger Games","A really real reality show","https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg","https://www.youtube.com/watch?v=4S9a5V9ODuY")

logan=media.Movie("Logan","Wolverine","https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                        "https://www.youtube.com/watch?v=Div0iP65aZo")

forestgump=media.Movie("Forrest Gump","The World will never be the same once you see it throught the eyes of Forrest Gump","https://upload.wikimedia.org/wikipedia/sco/6/67/Forrest_Gump_poster.jpg",
                        "https://www.youtube.com/watch?v=uPIEn0M8su0")

castaway=media.Movie("Cast Away","At the edge of the world, his journey begins","https://upload.wikimedia.org/wikipedia/en/a/a7/Cast_away_film_poster.jpg",
                        "https://www.youtube.com/watch?v=PJvosb4UCLs")

davincicode=media.Movie("The da vinci code","Seek the Truth","https://upload.wikimedia.org/wikipedia/en/e/e9/The_da_vinci_code_final.jpg",
                        "https://www.youtube.com/watch?v=-rMElSGZpV4")
movies=[ratatoullie, transformers, logan, forestgump, castaway, davincicode]
fresh_tomatoes.open_movies_page(movies)
