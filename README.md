# LinkDN

LinkDN is an aspiring social media site exclusive to Del Norte's students. Students can share their "stats," what classes they are taking, and their accomplishments outside of school. Ideally, LinkDN will be able to be used as a platform for students to create study/support groups with one another. 

#### How to Run

For now, clone our repository on your machine and run main.py. Website will be deployed ASAP. 

[Project Plan](https://docs.google.com/document/d/1FGxx_jWIMwzBsvnnm7vjAKN-VX4sEd5dISR_Y26ovc8/edit)

## Focus for this week

Please view the "issues" section of this repository to look at what we're focusing on this week and what has been deployed. Here is a hyperlink:

[Issues Page](https://github.com/Mewe14/P3Platypodes/issues)

## Key Features

#### Signup/Login page with Users database / Profile Page (Crystal Widjaja)

Users will be able to view their personal profile page, which includes the data they provided when signing up for their accounts. They will also be able to augment information, such as GPA and recent awards. Profiles will be able to be viewed by other users. The profile page utilizes html and css for the front end. Front end work can be found through the signup.html, login.html, and profile.html. The backend is planned to use apis and routing to gather information from the signup page to the profile page. In order to create the backend, we linked our sign up page to a user API which stores the information for each new signup. This utilizes SQL Alchemy and Python Routing to successfully transfer the information. The information can be accessed through the settings.py, api.html, main.py, and custom.py for the backend. 

#### About Page

Users can connect with the creators of the website and see their minilabs from this trimester.

#### Friends feature

Users will be able to reach out to other Del Norte students, perhaps through sending a small "This user wants to study with you!" message. 


## Mini Lab 1

#### Crystal's Classes Mini Lab

1. Blueprints are located in the classes directory
2. Classes can be found in this section of code:
   ````
   def math_class(self):
   limit = self._series
   f = [(random.sample((math_classes), k=2))]  # fibonacci starting array/list
   while limit > 0:
   self.set_data(f[0])
   f = [f[0]]
   limit -= 1
3. I created the object math from my class mathematics
   ````
       math = mathematics(a/a)
    print(f"Here are some math recommendations = {math.list}")
4. Used getters in allclass.html
5. This project helped give me insights on connecting blueprints with classes and objects. Furthermore, the mini-lab works very effectively with our projects focus and theme.  

#### Ida's Classes Mini Lab

1. My blueprint is located in the clubs directory.
2. I define a class here: 
   ````
   class Clubs:
    def __init__(self, name, media):
        self.name = name
        self.media = media

    def get_name(self):
        return self.name

    def get_media(self):
        return self.media
3. I created several Clubs objects and placed them in a featuredclubs list. Eventually, I will have a local API of clubs at Del Norte and the list will be generated.
   ````
   thetalon = Clubs('The Talon', 'https://www.dntalon.com')
   girlsincs = Clubs('Girls in Computer Science', 'https://www.instagram.com/girlsincs/')
   trim = Clubs('Tri-M Music Honor Society', 'https://linktr.ee/dnhstrim')
   bsu = Clubs('Black Student Union', 'https://www.instagram.com/dnhsbsu/')
4. Transferred list into app.py in clubs blueprint. Attributes of class accessed and displayed in Jinja loop.
   ````
   {% for club in featuredclubs %}
        <li><a href="{{ club.media }}">{{ club.name }}</a></li></li>
    {% endfor %}
5. My WOW factor is displaying the class objects using a for loop and accessing their attributes via html/Jinja, specifically in how I link the featured clubs' websites. This project gave me insight into how blueprints can assist in compartmentalizing code, as well as the use of classes when I will eventually be managing a much larger data set.
#### Sophie's Classes Mini Lab
The wow factor is displaying both the greatest common denominator and least common multiple each time you change a and b, having it visible on the website and knowing how to include mathematical algorithms in my project. The first binary point of using an individual blueprint for my scrum team project can be shown through the minilabs. html file where I set up a table for each group members code to be organized. My blueprints can also be found in the administration directory. The second binary point says to define a class to manage a complex data set, which is shown in line 4 of the code where I define a class as Least Common Multiple. The third binary point comes from creating an object from a class in python, which is shown in line 31 which creates a class object. The 4th binary point comes from displaying data using getters which is shown in lines 19 and 23 when I write @property.  </h2>

## Feedback Page (Made by Sophie)
In order to create the feedback page, we used a Jinja template and formatted it so that the user could input their information and give the creators imput on how we could better format the website so that it easier to navigate and use. The Jinja template allows us to customize tests and quizzes. It also allows the website designer to call functions with arguments. We allowed the user to give us background into who they are so we could better get an understanding of who are audience is.

This shows the format for making the jinja template:

<h1>Feedback Form</h1>

<div class="container">
    <form action="/Responses/">
        <label for="fname">First Name</label>
        <input type="text" id="fname" name="firstname" placeholder="first name..">

        <label for="lname">Last Name</label>
        <input type="text" id="lname" name="lastname" placeholder="last name..">

        <label for="Grade">Grade</label>
        <select id="grade" name="grade">
            <option value="9">9</option>
            <option value="10">10</option>
            <option value="11">11</option>
            <option value="12">12</option>
        </select>
        <label for="subject">Feedback</label>
        <textarea id="subject" name="subject" placeholder="What feedback would you like to provide us with?" style="width: 500px;"></textarea>

        <input type="submit" value="Submit">
    </form>
</div>

## Quiz Page (Made by Sophie)
In order to create this quiz page I first picked an API that would give the user insight into what college would be best suited for them since the main purpose of our website is to help DN students with their educational careers. We dowloaded the API locally and query'd the database with static endpoints sothat the user would input answers to the quiz questions and get a list of possible colleges that is in accordance with the answers they chose. I used one template and repopulated that template with different questions, instead of creating a new page everytime the user moves on. I did this by creating routes, and each button is a route, so every time you press the next different, a new set of data is filtered through the template. The output gives links to colleges that the quiz determined are good for you in order to provide more information so that the user can make the most informed decisions possible.

this shows important code for getting the results:
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
    

## Creators

Sophie Bulkin, Ida Mobini, Arul Salaniwal, Manuel Villa-Hernandez, Crystal Widjaja
