import media
import fresh_tomatoes

harry_potter1 = media.Movie("Harry Potter and the Sorcerer's Stone",
                            "Rescued from the outrageous neglect of his aunt and uncle, a young boy with a great destiny proves his worth while attending Hogwarts School of Witchcraft and Wizardry.",
                            "http://ia.media-imdb.com/images/M/MV5BMTYwNTM5NDkzNV5BMl5BanBnXkFtZTYwODQ4MzY5._V1_SX640_SY720_.jpg",
                            "https://www.youtube.com/watch?v=PbdM1db3JbY")

harry_potter2 = media.Movie("Harry Potter and the Chamber of Secrets",
                            "Harry ignores warnings not to return to Hogwarts, only to find the school plagued by a series of mysterious attacks and a strange voice haunting him.",
                            "http://cdn.movieclips.com/keyart/206646x480.jpg",
                            "https://www.youtube.com/watch?v=uU-ET1FAv3Y")

harry_potter3 = media.Movie("Harry Potter and the Prisoner of Azkaban",
                            "It's Harry's third year at Hogwarts; not only does he have a new \"Defense Against the Dark Arts\" teacher, but there is also trouble brewing. Convicted murderer Sirius Black has escaped the Wizards' Prison and is coming after Harry.",
                            "http://static.rogerebert.com/uploads/movie/movie_poster/harry-potter-and-the-prisoner-of-azkaban-2004/large_7VTALkqjG40vby3uVIsp03d7yXy.jpg",
                            "https://www.youtube.com/watch?v=R69laoH02xg")

harry_potter4 = media.Movie("Harry Potter and the Goblet of Fire",
                            "Harry finds himself mysteriously selected as an under-aged competitor in a dangerous tournament between three schools of magic.",
                            "http://ia.media-imdb.com/images/M/MV5BMTI1NDMyMjExOF5BMl5BanBnXkFtZTcwOTc4MjQzMQ@@._V1_SX640_SY720_.jpg",
                            "https://www.youtube.com/watch?v=PFWAOnvMd1Q")

harry_potter5 = media.Movie("Harry Potter and the Order of the Phoenix",
                            "With their warning about Lord Voldemort's return scoffed at, Harry and Dumbledore are targeted by the Wizard authorities as an authoritarian bureaucrat slowly seizes power at Hogwarts.",
                            "http://img3.wikia.nocookie.net/__cb20120525191100/harrypotter/images/5/5f/-Harry-Potter-and-the-Order-of-the-Phoenix.jpg",
                            "https://www.youtube.com/watch?v=vz2_xS4TN6w")

harry_potter6 = media.Movie("Harry Potter and the Half-Blood Prince",
                            "As Harry Potter begins his sixth year at Hogwarts, he discovers an old book marked as \"the property of the Half-Blood Prince\" and begins to learn more about Lord Voldemort's dark past.",
                            "http://www.gstatic.com/tv/thumb/dvdboxart/176377/p176377_d_v8_aa.jpg",
                            "https://www.youtube.com/watch?v=jpCPvHJ6p90")

harry_potter7 = media.Movie("Harry Potter and the Deathly Hallows - Part 1",
                            "As Harry races against time and evil to destroy the Horcruxes, he uncovers the existence of three most powerful objects in the wizarding world: the Deathly Hallows.",
                            "http://ia.media-imdb.com/images/M/MV5BMTQ2OTE1Mjk0N15BMl5BanBnXkFtZTcwODE3MDAwNA@@._V1_SX640_SY720_.jpg",
                            "https://www.youtube.com/watch?v=Jr9OQROqxzE")

harry_potter8 = media.Movie("Harry Potter and the Deathly Hallows - Part 2",
                            "Harry, Ron and Hermione search for Voldemort's remaining Horcruxes in their effort to destroy the Dark Lord as the final battle rages on at Hogwarts.",
                            "http://t3.gstatic.com/images?q=tbn:ANd9GcTgXSuLAFerQGZdPCWv8EHI_ucQq6RTl3xf91F4aN54PDA_oCtB",
                            "https://www.youtube.com/watch?v=_EC2tmFVNNE")


movies = [harry_potter1, harry_potter2, harry_potter3, harry_potter4,
          harry_potter5, harry_potter6, harry_potter7, harry_potter8]
#fresh_tomatoes.open_movies_page(movies)
#print media.Movie.VALID_RATINGS
print media.Movie.__doc__
