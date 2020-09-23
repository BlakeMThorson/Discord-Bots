import pickle


def getMovie(fuck):
    fuck = fuck.capitalize()
    
    if fuck not in ['Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']:

        return "NOW YOU FUCKED UP"
    
    else:
        import random
        toReturn = pickle.load(open("genreSorted.pickle", "rb"))
        return random.choice(toReturn[fuck])


def trueRandom():
    import random
    toReturn = pickle.load(open("genreSorted.pickle", "rb"))
    
    return random.choice(toReturn[ random.choice(['Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']) ]) 


def formatter(myList):
    x = {
        'Action': "<:action:643387530170990610>", 
        'Adult': "<:adult:643387530586357760>", 
        'Adventure': "<:adventure:643387530582032384>", 
        'Animation': "<:animation:643387530573512714>", 
        'Biography': "<:biography:643387530351476747>", 
        'Comedy': "<:comedy:643387530523312149>", 
        'Crime': "<:crime:643387530594484224>", 
        'Documentary': "<:documentary:643387530691215360>", 
        'Drama': "<:drama:643387530594615336>", 
        'Family' : "<:family2:643387530255007756>", 
        'Fantasy': "<:fantasy:643387530229579778>", 
        'Film-Noir': "<:filmnoir:643387530678370304>", 
        'History': "<:history:643387530640752660>", 
        'Horror': "<:horror:643387530716250112>", 
        'Music' : "<:music:643387530691084318>", 
        'Musical' : "<:music:643387530691084318>", 
        'Mystery' : "<:mystery:643387530682564609>", 
        'News' : "<:news:643387530707730441>", 
        'Reality-TV' : "<:realitytv:643387530838016001>", 
        'Romance': "<:romance:643387530699603978>", 
        'Sci-Fi' : "<:scifi:643387531085217802>", 
        'Short': "<:short:643387530359865345>", 
        'Sport': "<:sport:643387530724638750>", 
        'Thriller' : "<:thriller:643387530909188116>", 
        'War' : "<:war:643387530942742539>", 
        'Western' : "<:western:643387530531700748>"
    }
    
    x1 = []
    for i in myList:
        x1.append("{} {}".format(x[i], i))
    return x1
        


