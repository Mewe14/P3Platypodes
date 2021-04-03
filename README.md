# LinkDN

LinkDN is an aspiring social media site exclusive to Del Norte's students. Students can share their "stats," what classes they are taking, and their accomplishments outside of school. Ideally, LinkDN will be able to be used as a platform for students to create study/support groups with one another. 

[Project Plan](https://docs.google.com/document/d/1FGxx_jWIMwzBsvnnm7vjAKN-VX4sEd5dISR_Y26ovc8/edit)
## Key Features

#### Signup/Login page with Users database

Users will be able to create an account with personal data such as name, age, and graduating year, which will be stored in a database. They will then be able to sign into their accounts and view their unique profiles. 

#### Profile page

Users will be able to view their personal profile page, which includes the data they provided when signing up for their accounts. They will also be able to augment information, such as GPA and recent awards. Profiles will be able to be viewed by other users. 

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

## Creators

Sophie Bulkin, Ida Mobini, Arul Salaniwal, Manuel Villa-Hernandez, Crystal Widjaja
