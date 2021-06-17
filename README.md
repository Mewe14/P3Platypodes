# LinkDN

LinkDN is an aspiring social media site exclusive to Del Norte's students. Students can share their "stats," what classes they are taking, and their accomplishments outside of school. Ideally, LinkDN will be able to be used as a platform for students to create study/support groups with one another. 

## Final Grading

#### +5 Theme Section (No Login or Easy Guest access) 5/5

Theme Colors: Blue and Green / Themed to be like LinkedIn

Technicals: Sign Up Page, Login Page, About Page, Sophie’s Minilab, Classes Page, Club Page (+3)

Interactions: College Quiz Page, Contact Page, Feedback Page (+1.5)

Creative: College Quiz, About Us Page (+2)

#### +5 API Section 5/5
API used for the college quiz 

Crossed over with Team Parrots who helped us set up the APIs

Utilized their same school API +2

Created our own user profiles API +2

Style with CSS (+1)

#### +5 Deployment Section 5/5
Quality and Usability of Project

ReadMe / Scrum Board (+2)

Commercial Video (+3)

### +5 Individual Grading
Crystal 4.5/5 --> Labs: Bubble Sort and Binary Search    Technicals:Login page, Sign Up Page, Styling for Quiz Page, User API, Classes (+2.5)


Sophie 4/5 --> Labs: Finding the LCM/GCD of two integers and Bubble Sort/explanation of how bubble sort works (+2)      Technicals: Quiz Page/Api, Feedback page, Individual page, About page/styling (+2)


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

## Sophie's Bubble Sort Mini Lab
The purpose of the bubble sort mini lab is to create a bubble sort which swaps different elements if they are in the wrong order in order to educate the target audience of young children how to correctly sort numbers. When you press the submit button, it generates an output with the information that you inputted in the correct numerical order. The input is entering the a list of numbers, and the output is the same numbers being laid out in numerical order. 
This code shows how the data from the list that was created is being used:
 from math import gcd

        class LeastCommonMultiple: ##this is where I define a class

            def __init__(self, a,b):
                self._multiple = self.lcm()
                self._denominator = self.gcd()

            def gcd(self):
                if a == 0:
                    return b
                return gcd(b % a, a)

            # Function to return LCM of two numbers
            def lcm(self):
                return (a / gcd(a,b))* b

            @property
            def leastcommon_multiple(self):
                return self._multiple

            @property
            def denominator(self):
                return self._denominator

The data contained in the list represents the information that will be tested in the driver code in order to print a sorted array. The List generates the the information inputted in numerical order based on what they entered, the sorty  parameter sets restrictions to the algorithm. 
The way that the algorithm works is that bubble has 2 parameters, value and sorty. Beneath the class, we have constructed and initiated a series. We then define the parameter sirt which sets restrictions to the algorithm. The class bubble is where the algorithm builds the series. If the user inputs a list of numbers into the textbox field separated by a comma, it will output a list of numbers that follow the conditions that these two parameters have setup. It will then give the values in the correct order for the information that the user inputted. The bubble sort does this by comparing two elements at a time, and if one is greater than the other, it will switch the elements. This process repeats with each element until they’re in the proper order

    def bubbleSort(value_1):
        n = len(value_1)-3
        value_sorty = value_1
        arr = value_sorty.split(',')
        value = arr

        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n-i-1):
                if value[j] > value[j+1]:
                    value[j], value[j+1] = value[j+1], value[j]

It will test what information the user is inputting and pass the values through the correct algorithm in order to produce a value in the correct order and range. It tests what information could be processed by the algorithm according to the input of numbers by the user

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

#### Manuel's Classes Mini Lab
The wow factor is displaying both x and y values that satisfy the equation ax + by = n, having it visible on the website and knowing how to include mathematical algorithms in my project. The first binary point of using an individual blueprint for my scrum team project can be shown through the minilabs.  The second binary point says to define a class to manage a complex data set, which is shown in the code where I define a class as Solution. The third binary point comes from creating an object from a class in python. The 4th binary point comes from displaying data which is shown by outputting the x and y that satisfy the equation, or it outputs "no solution".  </h2>

## About us Page (Made by Manuel)
The about us page was created using python and css to style it, we added the ability to embed journals into the page so that users can learn more about the creators of the website, we also added the ability to contact each creator via email and has a navbar so the user can find each person quickly and easily.

Here is some example code of one of our creators in the about us page:

<section id="manuel" style="w3-cyan width:100%">
        <div align="center" style="w3-cyan width:100%" >
            <h5 class="w3-center w3-padding-5" style="font-family:Roboto; font-size: 40px" ><span class="w3-tag w3-green">MANUEL</span></h5>
            <iframe src="https://docs.google.com/document/d/1jMtzi4i17i17SYjVa3cnJK06rem81XqqCBozq5FvPXc/edit" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe></iframe>
        </div>
       # <h2>Contact Manuel through e-mail!</h2>
        #<form action="mailto:mvvillah@icloud.com" method="post" enctype="text/plain">
           #  <br>
            #<input type="text" name=" "><br>
            #Name:<br>
           # <input type="text" name="name"><br>
           # E-mail:<br>
           # <input type="text" name="mail"><br>
            #Comment:<br>
           # <input type="text" name="comment" size="50"><br><br>
            #<input type="submit" value="Send">
            #<input type="reset" value="Reset">
       # </form>
   # </section>

    

## Creators

Sophie Bulkin, Ida Mobini, Arul Salaniwal, Manuel Villa-Hernandez, Crystal Widjaja
