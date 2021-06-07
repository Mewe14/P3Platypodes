import sqlite3
import json

# https://collegescorecard.ed.gov/data/documentation/

conn = sqlite3.connect('schools.db')

crs = conn.cursor()

# def construct_query(region, locale)

#for row in conn.execute("select name, city, state, url, locale, carnegie_basic from schools where city in ('Denver', "
                       # "'Aurora') and carnegie_basic < 12"):
    #print(row)


def where_locale(answer):
    if answer == "1":
        return "locale >= 11 and locale <= 13"
    if answer == "2":
        return "locale >= 21 and locale <= 23"
    if answer == "3":
        return "locale >= 31 and locale <= 33"
    if answer == "4":
        return "locale >= 41 and locale <= 43"


def where_state(answer):
    if answer == "1":
        return "state in ('CT', 'ME', 'MA', 'NH', 'RI', 'VT')"
    if answer == "2":
        return "state in ('DE', 'DC', 'MD', 'NJ', 'NY', 'PA')"
    if answer == "3":
        return "state in ('IL', 'IN', 'MI', 'OH', 'WI')"
    if answer == "4":
        return "state in ('IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD')"
    if answer == "5":
        return "state in ('AL', 'AR', 'FL', 'GA', 'KY', 'LA', 'MS', 'NC', 'SC', 'TN', 'VA', 'WV')"
    if answer == "6":
        return "state in ('AZ', 'NM', 'OK', 'TX')"
    if answer == "7":
        return "state in ('CO', 'ID', 'MT', 'UT', 'WY')"
    if answer == "8":
        return "state in ('AK', 'CA', 'HI', 'NV', 'OR', 'WA')"
    if answer == "9":
        return "state in ('AS', 'FM', 'GU', 'MH', 'MP', 'PR', 'PW', 'VI')"
    return ""


def where_carnegie_basic(answer):
    if answer == "1":
        return "carnegie_basic >= 1 and carnegie_basic <= 9"
    if answer == "2":
        return "carnegie_basic >= 15 and carnegie_basic <= 17"
    if answer == "3":
        return "carnegie_basic >= 18 and carnegie_basic <= 20"
    if answer == "4":
        return "carnegie_basic >= 21 and carnegie_basic <= 23"
    if answer == "5":
        return "(carnegie_basic >= 10 and carnegie_basic <= 13) or" \
               " (carnegie_basic >= 24 and carnegie_basic <= 32)"
    return ""


def where_carnegie_basic2(answer):
    if answer == "1":  # STEM
        return "((carnegie_basic >= 4 and carnegie basic <= 11) or (carnegie_basic = 17) or (carnegie_basic >= 25 and " \
               "carnegie_basic <= 28)) "
    if answer == "2":  # LSA
        return "((carnegie_basic >= 1 and carnegie_basic <= 3) or (carnegie basic >= 18 and carnegie_basic <= 22))"
    if answer == "3":  # Art
        return "(carnegie_basic = 12 or carnegie_basic = 30)"
    if answer == "4":  # Research
        return "(carnegie_basic = 15 or carnegie_basic = 16)"
    if answer == "5":  # Law
        return "carnegie_basic = 31"
    if answer == "6":  # N/A
        return "carnegie_basic = -2"
    if answer == "7":  # Undeclared/Other
        return "(carnegie_basic = 0 or carnegie_basic = 13 or carnegie_basic = 24 or carnegie_basic = 32)"
    return ""


def where_ownership(answer):
    if answer == "1":
        return "ownership = 1"
    if answer == "2":
        return "(ownership = 2 or ownership = 3)"
    if answer == "3":
        return "ownership >= 1 and ownership <= 3"
    return ""


def where_carnegie_undergrad(answer):
    if answer == "1":
        return "carnegie_undergrad >= 1 and carnegie_undergrad <= 4"
    if answer == "2":
        return "carnegie_undergrad >= 5 and carnegie_undergrad <= 15"
    if answer == "3":
        return "carnegie_undergrad = 0"
    if answer == "4":
        return "carnegie_undergrad = -2"
    return ""


def query_colleges(answers):
    conn = sqlite3.connect('schools.db')
    answers_json = json.loads(answers)
    print(answers_json)
    where = where_locale(answers_json['0']) + " and " + \
            where_state(answers_json['1']) + " and " + \
            where_carnegie_basic(answers_json['4']) + " and " + \
            where_ownership(answers_json['2']) + " and " + \
            where_carnegie_undergrad(answers_json['5'])
    query = "select name, city, state, url, ownership from schools" \
            " where " + where
    print(query)
    result = []
    for row in conn.execute(query):
        # print(row)
        result.append(row)

    return result