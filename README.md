# Django-Blog Site 
<h4>
Create a superUser account before interacting with User, Account, Model and Admin Privilages
</h4>
<h2>
Main Features :
</h2>
<ul>
<li>Blog Page WIth Backend Dashboard</li>
<li>Pagination</li>
<li>Registration Page</li>
<li>Frondend and Backend Validation</li>
<li>Login Page With Password Recovery Options </li>
<li>After Login, User can Create, Update and Delete Their Posts</li>
<li>After Login, User can update Their Profile Info Like (E-mail , Username and Profile Pictures) </li>
<li>Number of Posts By a Specific User Shown with Pagination </li>
<li>Admin Panel only for SuperUser</li>
</ul>

<h2>
Used Technolgies :
</h2>
<ul>
<li>Python</li>
<li>Django v2.2.1</li>
<li>SQLite3</li>
<li>HTML</li>
<li>CSS</li>
<li>Bootstrap</li>
<li>Crispy Form</li>
<li>Font-Awesome</li>
<li>JavaScript</li>
</ul>

<h2>Installation</h2>
<h4>Create WebBlog virtual environment & goto the directory.
</h4>

<h4>
Linux -->
</h4>
<div>
virtualenv -p /usr/bin/python3 WebBlog
cd WebBlog/
</div>



<h4>
Windows -->
</h4>
<div>
virtualenv WebBlog
cd .\WebBlog\
</div>


<h2>Activate virtualenv :</h2>
<h4>Linux -->
</h4>
<div>
source bin/activate
</div>


<h4>Windows--></h4>
<div>
.\Scripts\activate
</div>

<h2>
clone the project in the WebBlog directory.
</h2>

<div>
git clone https://github.com/sohanur-it/Django-Blog.git
</div>

<h2>Install requirements.txt
</h2>
<div>
python -m pip install -r requirements.txt
</div>
<h2>
Now goto src/ directory and create db models.
</h2>


<div>
cd src/
python manage.py migrate
</div>

<h2>Run Server :</h2>
<div>
python manage.py runserver
</div>
<a href="http://127.0.0.1:8000/"><ul><li>now goto http://127.0.0.1:8000/</li></ul> </a>



<h2>Scrrenshots : </h2>
<br>
<img src='https://github.com/sohanur-it/Django-Blog/blob/master/src/screenshot/django-blog.png'>
<br><br>

<br>
<img src='https://github.com/sohanur-it/Django-Blog/blob/master/src/screenshot/register.png'>
<br><br>


<br>
<img src='https://github.com/sohanur-it/Django-Blog/blob/master/src/screenshot/login.png'>
<br><br>
