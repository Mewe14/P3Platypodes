import sqlite3
import json

conn = sqlite3.connect('schools.db')

crs = conn.cursor()

# school.name,school.city,school.state,school.zip,school.carnegie_size_setting,school.school_url,school.carnegie_basic,school.locale,school.region_id,school.ownership,school.carnegie_undergrad
crs.execute('''create table schools (
                 name text,
                 city text,
                 state text,
                 url text,
                 region_id integer,
                 locale integer,
                 carnegie_size_setting integer,
                 carnegie_basic integer,
                 carnegie_undergrad integer,
                 ownership integer)''')


def insert_school(school):
    locale = str(school['school.locale']) if school['school.locale'] else 'null'
    carnegie_size_setting = str(school['school.carnegie_size_setting']) if school['school.carnegie_size_setting'] else 'null'
    carnegie_basic = str(school['school.carnegie_basic']) if school['school.carnegie_basic'] else 'null'
    carnegie_undergrad = str(school['school.carnegie_undergrad']) if school['school.carnegie_undergrad'] else 'null'
    ownership = str(school['school.ownership']) if school['school.ownership'] else 'null'
    url = '"' + school['school.school_url'] + '"' if school['school.school_url'] else 'null'
    query = 'insert into schools values(' + \
            '"' + school['school.name'] + '", ' + \
            '"' + school['school.city'] + '", ' + \
            '"' + school['school.state'] + '", ' + \
            url + ', ' + \
            str(school['school.region_id']) + ', ' + \
            locale + ', ' + \
            carnegie_size_setting + ', ' + \
            carnegie_basic + ', ' + \
            carnegie_undergrad + ', ' + \
            ownership + ")"
    print(query)
    crs.execute(query)


def process_file(file_name):
    with open(file_name) as f:
        data = json.load(f)
    for school in data['results']:
        insert_school(school)


for file in range(68):
    print('Reading file #' + str(file))
    file_name = 'schools/school-' + str(file) + '.json'
    process_file(file_name)

conn.commit()
conn.close()