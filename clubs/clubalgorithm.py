class Clubs:
    def __init__(self, name, media):
        self.name = name
        self.media = media

    def get_name(self):
        return self.name

    def get_media(self):
        return self.media

featuredclubs = []

featuredclubs.append(Clubs('The Talon', 'dntalon.com'))
featuredclubs.append(Clubs('Girls in Computer Science', 'https://www.instagram.com/girlsincs/'))
featuredclubs.append(Clubs('Tri-M Music Honor Society', 'https://linktr.ee/dnhstrim'))
featuredclubs.append(Clubs('Black Student Union', 'https://www.instagram.com/dnhsbsu/'))