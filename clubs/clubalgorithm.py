import csv

clubsfile = open('clubs/static/clubstest.csv')
clubsreader = csv.reader(clubsfile)
clubsdata = list(clubsreader)

class Clubs:
    def __init__(self, name, media):
        self.name = name
        self.media = media

    def get_name(self):
        return self.name

    def get_media(self):
        return self.media

clubslist = [Clubs(club[1], club[2]) for club in clubsdata]
# for club in clubslist:
    # print(club.get_name())