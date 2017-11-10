#Importing modules and files as necessary
import fresh_tomatoes
import media

#Defining various instances(Movies) of Movie Class below. 
ratatoullie=media.Movie("Ratatoullie","A story of a Rat and his love for cooking","https://54disneyreviews.files.wordpress.com/2015/07/ratatouille1.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")
transformers=media.Movie("Transformers","Autobots and the Decepticons","https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",
                        "https://www.youtube.com/watch?v=dxQxgAfNzyE")
logan=media.Movie("Logan","Wolverine","https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                        "https://www.youtube.com/watch?v=Div0iP65aZo")
forestgump=media.Movie("Forrest Gump","The World will never be the same once you see it throught the eyes of Forrest Gump","https://upload.wikimedia.org/wikipedia/sco/6/67/Forrest_Gump_poster.jpg",
                        "https://www.youtube.com/watch?v=uPIEn0M8su0")
castaway=media.Movie("Cast Away","At the edge of the world, his journey begins","https://upload.wikimedia.org/wikipedia/en/a/a7/Cast_away_film_poster.jpg",
                        "https://www.youtube.com/watch?v=PJvosb4UCLs")
davincicode=media.Movie("The da vinci code","Seek the Truth","https://upload.wikimedia.org/wikipedia/en/e/e9/The_da_vinci_code_final.jpg",
                        "https://www.youtube.com/watch?v=-rMElSGZpV4")

#Defining a list with all the instaces created above
movies=[ratatoullie, transformers, logan, forestgump, castaway, davincicode]

#Passing the list of movies to Freshtomatoes File
fresh_tomatoes.open_movies_page(movies)
