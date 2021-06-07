import model


def setup():
    question1 = model.Question("What is your weighted GPA?", "1.0 - 2.0", "2.0 - 3.0", "3.0 - 4.0", "4.0+")

    question2 = model.Question("What is your ideal location?", "East Coast", "West Coast", "Central", "No Preference")

    question3 = model.Question("What do you want a main focus of your campus to be?", "Education", "Sports", "Greek Life", "Other/No Preference")

    question4 = model.Question("What is your budget per year?", "Less than 15k", "15-25k", "25-35k", "35k+")

    question5 = model.Question("What majors/areas of study are you most interested in?", "STEM", "English/Journalism/History", "Fine Arts", "Other/Undecided")
