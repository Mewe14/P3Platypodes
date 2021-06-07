from query import query_colleges

class Answer:
    def __init__(self, answer_index, answer_text):
        self.index = answer_index
        self.text = answer_text


class Question:
    def __init__(self, index, question, answers):
        self.index = index
        self.question = question
        self.answers = answers


questions = [
    Question(1, "What do you prefer the environment to be?",
             [Answer(1, "City (Population: over 250,000)"),
              Answer(2, "Suburb (Population: 100,000 - 250,000)"),
              Answer(3, "Town (cluster 10 - 35 miles away from urban area)"),
              Answer(4, "Rural (5 - 25 miles away from urban area)")]),
    Question(2, "What is your ideal location?",
             [Answer(1, "New England (CT, ME, MA, NH, RI, VT)"),
              Answer(2, "Mid East (DE, DC, MD, NJ, NY, PA)"),
              Answer(3, "Great Lakes (IL, IN, MI, OH, WI)"),
              Answer(4, "Plains (IA, KS, MN, MO, NE, ND, SD)"),
              Answer(5, "Southeast (AL, AR, FL, GA, KY, LA, MS, NC, SC, TN, VA, WV)"),
              Answer(6, "Southwest (AZ, NM, OK, TX)"),
              Answer(7, "Rocky Mountains (CO, ID, MT, UT, WY)"),
              Answer(8, "Far West (AK, CA, HI, NV, OR, WA)"),
              Answer(9, "Outlying Areas (AS, FM, GU, MH, MP, PR, PW, VI)")]),
    Question(3, "Would you prefer a public or a private university?",
             [Answer(1, "Public"),
              Answer(2, "Private"),
              Answer(3, "No Preference")]),
    Question(4, "What majors/areas of study are you most interested in?",
             [Answer(1, "STEM"),
              Answer(2, "English/History/Business (LSA)"),
              Answer(3, "Fine Arts"),
              Answer(4, "Research Focus"),
              Answer(5, "Law"),
              Answer(6, "Not Applicable"),
              Answer(7, "Other/Undeclared")]),
    Question(5, "What degree are you looking to get in college?",
             [Answer(1, "Associates Degree"),
              Answer(2, "Doctorate"),
              Answer(3, "Master's Degree"),
              Answer(4, "Bachelor's Degree"),
              Answer(5, "2 Year / 4 Year Special Focus")]),
    Question(6, "How many years are you looking to spend in undergrad?",
             [Answer(1, "2 years"),
              Answer(2, "4 years"),
              Answer(3, "Exclusively Graduate"),
              Answer(4, "Not Applicable")]),
]


def quizdata():
    return questions


def handle_response(answers):
    print(answers)
    return query_colleges()
    return "thank you!"
