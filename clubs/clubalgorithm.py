class Clubs:
    def __init__(self, name, media):
        self.name = name
        self.media = media

    def get_name(self):
        return self.name

    def get_media(self):
        return self.media

featuredclubs = []

thetalon = Clubs('The Talon', 'dntalon.com')
girlsincs = Clubs('Girls in Computer Science', 'https://www.instagram.com/girlsincs/')
trim = Clubs('Tri-M Music Honor Society', 'https://linktr.ee/dnhstrim')
bsu = Clubs('Black Student Union', 'https://www.instagram.com/dnhsbsu/')

featuredclubs.append(thetalon)
featuredclubs.append(girlsincs)
featuredclubs.append(trim)
featuredclubs.append(bsu)

# print(thetalon.media)
# Eventually I will have a local API of clubs at our school and the featured clubs list will be randomly selected
# Can class objects be created automatically?