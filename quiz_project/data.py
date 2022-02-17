question_data = [
    {"category": "Entertainment: Cartoon & Animations", "type": "multiple", "difficulty": "medium",
     "question": "Which &quot;Toy Story&quot; character was voiced by Don Rickles?",
     "correct_answer": "Mr. Potato Head", "incorrect_answers": ["Slinky Dog", "Hamm", "Rex"]},
    {"category": "Science & Nature", "type": "multiple", "difficulty": "easy",
     "question": "Which type of rock is created by intense heat AND pressure?", "correct_answer": "Metamorphic",
     "incorrect_answers": ["Sedimentary", "Igneous", "Diamond"]},
    {"category": "Entertainment: Music", "type": "multiple", "difficulty": "easy",
     "question": "Who is the lead singer of Pearl Jam?", "correct_answer": "Eddie Vedder",
     "incorrect_answers": ["Ozzy Osbourne", "Stone Gossard", "Kurt Cobain"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "easy",
     "question": "What is Pikachu&#039;s National Pok&eacute;Dex Number?", "correct_answer": "#025",
     "incorrect_answers": ["#001", "#031", "#109"]},
    {"category": "Science & Nature", "type": "multiple", "difficulty": "medium",
     "question": "To the nearest minute, how long does it take for light to travel from the Sun to the Earth?",
     "correct_answer": "8 Minutes", "incorrect_answers": ["6 Minutes", "2 Minutes", "12 Minutes"]},
    {"category": "Science & Nature", "type": "multiple", "difficulty": "easy",
     "question": "What is the powerhouse of the cell?", "correct_answer": "Mitochondria",
     "incorrect_answers": ["Ribosome", "Redbull", "Nucleus"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
     "question": "Unturned originally started as a Roblox game.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Mythology", "type": "multiple", "difficulty": "easy",
                                       "question": "Who was the King of Gods in Ancient Greek mythology?",
                                       "correct_answer": "Zeus", "incorrect_answers": ["Apollo", "Hermes", "Poseidon"]},
    {"category": "Geography", "type": "multiple", "difficulty": "easy",
     "question": "What is the official language of Costa Rica?", "correct_answer": "Spanish",
     "incorrect_answers": ["English", "Portuguese", "Creole"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "easy",
     "question": "Which of these is NOT a playable character in the 2016 video game Overwatch?",
     "correct_answer": "Invoker", "incorrect_answers": ["Mercy", "Winston", "Zenyatta"]},
    {"category": "General Knowledge", "type": "multiple", "difficulty": "medium",
     "question": "What is the Swedish word for &quot;window&quot;?", "correct_answer": "F&ouml;nster",
     "incorrect_answers": ["H&aring;l", "Sk&auml;rm", "Ruta"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "medium",
     "question": "In Left 4 Dead, what is the name of the Special Infected that is unplayable in Versus mode?",
     "correct_answer": "The Witch", "incorrect_answers": ["The Tank", "The Smoker", "The Spitter"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "easy",
     "question": "In Portal 2, how did CEO of Aperture Science, Cave Johnson, presumably die?",
     "correct_answer": "Moon Rock Poisoning",
     "incorrect_answers": ["Accidentally sending a portal to the Moon", "Slipped in the shower", "Asbestos Poisoning"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "easy",
     "question": "Which of these characters is the mascot of the video game company SEGA?",
     "correct_answer": "Sonic the Hedgehog", "incorrect_answers": ["Dynamite Headdy", "Alex Kidd", "Opa-Opa"]},
    {"category": "Entertainment: Japanese Anime & Manga", "type": "multiple", "difficulty": "medium",
     "question": "What song plays in the ending credits of the anime &quot;Ergo Proxy&quot;?",
     "correct_answer": "Paranoid Android",
     "incorrect_answers": ["Sadistic Summer", "Bittersweet Symphony", "Mad World"]},
    {"category": "Entertainment: Television", "type": "multiple", "difficulty": "easy",
     "question": "In Game of Thrones, what is Littlefinger&#039;s real name?", "correct_answer": "Petyr Baelish",
     "incorrect_answers": ["Podrick Payne", "Lancel Lannister", "Torrhen Karstark"]},
    {"category": "History", "type": "multiple", "difficulty": "medium",
     "question": "What were the first states to break away from Yugoslavia?", "correct_answer": "Slovenia, Croatia",
     "incorrect_answers": ["Macedonia, Montenegro", "Slovenia, Macedonia", "Montenegro, Slovenia"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "medium",
     "question": "The protagonist in the game &quot;Cave Story&quot; is named", "correct_answer": "Quote",
     "incorrect_answers": ["Kazuma", "Curly", "Arthur"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "The Lego Group was founded in 1932.", "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "easy",
     "question": "Which of the following Elite Four members from the 6th Generation of Pok&eacute;mon was a member of Team Flare?",
     "correct_answer": "Malva", "incorrect_answers": ["Siebold", "Wikstrom", "Drasna"]},
    {"category": "Mythology", "type": "multiple", "difficulty": "easy",
     "question": "In most traditions, who was the wife of Zeus?", "correct_answer": "Hera",
     "incorrect_answers": ["Aphrodite", "Athena", "Hestia"]},
    {"category": "Geography", "type": "multiple", "difficulty": "hard",
     "question": "What is the Finnish word for &quot;Finland&quot;?", "correct_answer": "Suomi",
     "incorrect_answers": ["Eesti", "Magyarorsz&aacute;g", "Sverige"]},
    {"category": "Geography", "type": "multiple", "difficulty": "hard",
     "question": "When does Finland celebrate their independence day?", "correct_answer": "December 6th",
     "incorrect_answers": ["January 2nd", "November 12th", "February 8th"]},
    {"category": "Sports", "type": "multiple", "difficulty": "medium",
     "question": "What is the oldest team in the NFL?", "correct_answer": "Arizona Cardinals",
     "incorrect_answers": ["Chicago Bears", "Green Bay Packers", "New York Giants"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
     "question": "Which of the following is the oldest of these computers by release date?", "correct_answer": "TRS-80",
     "incorrect_answers": ["Commodore 64", "ZX Spectrum", "Apple 3"]},
    {"category": "Entertainment: Books", "type": "boolean", "difficulty": "hard",
     "question": "Harry Potter was born on July 31st, 1980.", "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Vehicles", "type": "multiple", "difficulty": "easy",
     "question": "Which car tire manufacturer is famous for its &quot;Eagle&quot; brand of tires, and is the official tire supplier of NASCAR?",
     "correct_answer": "Goodyear", "incorrect_answers": ["Pirelli", "Bridgestone", "Michelin"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
     "question": "Fast food restaurant chains Carl&#039;s Jr. and Hardee&#039;s are owned by the same company.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science & Nature", "type": "multiple", "difficulty": "hard",
     "question": "Botanically speaking, which of these fruits is NOT a berry?", "correct_answer": "Strawberry",
     "incorrect_answers": ["Blueberry", "Banana", "Concord Grape"]},
    {"category": "Entertainment: Television", "type": "multiple", "difficulty": "medium",
     "question": "What was Nickelodeon&#039;s original name?", "correct_answer": "Pinwheel",
     "incorrect_answers": ["MTVKids", "KidsTV", "Splat!"]},
    {"category": "General Knowledge", "type": "multiple", "difficulty": "easy",
     "question": "Which of the following card games revolves around numbers and basic math?", "correct_answer": "Uno",
     "incorrect_answers": ["Go Fish", "Twister", "Munchkin"]},
    {"category": "History", "type": "multiple", "difficulty": "medium",
     "question": "In World War I, what was the name of the alliance of Germany, Austria-Hungary, the Ottoman Empire, and Bulgaria?",
     "correct_answer": "The Central Powers",
     "incorrect_answers": ["The Axis Powers", "The Federation of Empires", "Authoritarian Alliance"]},
    {"category": "Entertainment: Television", "type": "multiple", "difficulty": "medium",
     "question": "What breed of dog is &quot;Scooby Doo&quot;?", "correct_answer": "Great Dane",
     "incorrect_answers": ["Pit bull", "Boxer", "Doberman Pinscher"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "medium",
     "question": "Which company developed and published Game Dev Tycoon?", "correct_answer": "Greenheart Games",
     "incorrect_answers": ["Greenland Games", "The Tycoonists", "MomCorp"]},
    {"category": "Celebrities", "type": "multiple", "difficulty": "medium",
     "question": "In which of these TV shows did the chef Gordon Ramsay not appear?",
     "correct_answer": "Auction Hunters",
     "incorrect_answers": ["Ramsay&#039;s Kitchen Nightmares", "Hotel Hell", "Hell&#039;s Kitchen"]},
    {"category": "Science: Mathematics", "type": "multiple", "difficulty": "easy",
     "question": "What is the correct order of operations for solving equations?",
     "correct_answer": "Parentheses, Exponents, Multiplication, Division, Addition, Subtraction",
     "incorrect_answers": ["Addition, Multiplication, Division, Subtraction, Addition, Parentheses",
                           "Parentheses, Exponents, Addition, Substraction, Multiplication, Division",
                           "The order in which the operations are written."]},
    {"category": "Entertainment: Japanese Anime & Manga", "type": "multiple", "difficulty": "easy",
     "question": "In Ms. Kobayashi&#039;s Dragon Maid, who is Kobayashi&#039;s maid?", "correct_answer": "Tohru",
     "incorrect_answers": ["Lucoa", "Kanna", "Elma"]},
    {"category": "Geography", "type": "multiple", "difficulty": "easy",
     "question": "Which ocean borders the west coast of the United States?", "correct_answer": "Pacific",
     "incorrect_answers": ["Atlantic", "Indian", "Arctic"]},
    {"category": "Entertainment: Board Games", "type": "multiple", "difficulty": "hard",
     "question": "What was the development code name for the &quot;Weatherlight&quot; expansion for &quot;Magic: The Gathering&quot;, released in 1997?",
     "correct_answer": "Mocha Latte", "incorrect_answers": ["Decaf", "Frappuccino", "Macchiato"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Nova Scotia is on the east coast of Canada.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "History", "type": "multiple", "difficulty": "hard",
                                       "question": "What was the last colony the UK ceded marking the end of the British Empire?",
                                       "correct_answer": "Hong Kong",
                                       "incorrect_answers": ["India", "Australia", "Ireland"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "easy",
     "question": "In the Halo series, which era of SPARTAN is Master Chief? ", "correct_answer": "SPARTAN-II",
     "incorrect_answers": ["SPARTAN-I", "SPARTAN-III", "SPARTAN-IV"]},
    {"category": "Celebrities", "type": "multiple", "difficulty": "hard",
     "question": "Who was Donald Trump&#039;s first wife?", "correct_answer": "Ivana Zeln&iacute;\u010dkov&aacute;",
     "incorrect_answers": ["Melania Knauss", "Marla Maples", "Nancy Davis"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "medium",
     "question": "What is the main character&#039;s name in &quot;Braid&quot;?", "correct_answer": "Tim",
     "incorrect_answers": ["Boregard", "James", "Jackson"]},
    {"category": "Entertainment: Cartoon & Animations", "type": "multiple", "difficulty": "hard",
     "question": "Benny, Brain, Fancy-Fancy, Spook and Choo-Choo were known associates of what Hanna Barbera cartoon character?",
     "correct_answer": "Top Cat", "incorrect_answers": ["Yogi Bear", "Snagglepuss", "Scooby-Doo"]},
    {"category": "Sports", "type": "multiple", "difficulty": "easy",
     "question": "Which African American is in part responsible for integrating  Major League baseball?",
     "correct_answer": "Jackie Robinson", "incorrect_answers": ["Curt Flood", "Roy Campanella", "Satchell Paige"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "medium",
     "question": "Which of the following is a character in the video game Destiny?", "correct_answer": "Cayde-6",
     "incorrect_answers": ["Ostrava of Boletaria", "Mordecai the Hunter", "Leon S. Kennedy"]},
    {"category": "Entertainment: Video Games", "type": "multiple", "difficulty": "easy",
     "question": "In the survival horror game, &quot;Cry of Fear,&quot; what was the name of Simon&#039;s close friend\/potential love interest?",
     "correct_answer": "Sophie", "incorrect_answers": ["Olivia", "Jessica", "Alice"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium", "question": "Is Tartu the capital of Estonia?",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Comics", "type": "multiple", "difficulty": "hard",
     "question": "What are the Three Virtues of Bionicle?", "correct_answer": "Unity, Duty, Destiny",
     "incorrect_answers": ["Build, Play, Change", "Work, Play, Live", "Forge, Build, Fight"]}
]
