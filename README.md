# (Main Branch consist of full code)
# Django_Web_Development

## For django tutorials : <a href = "https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p">👉CLICK</a>

## For NLP Based Scraping Bot : <a href = "https://www.youtube.com/watch?v=bjw8187Wi9o&t=20s">👉CLICK</a>

## Meetings Recording<a href="https://www.youtube.com/playlist?list=PLuZl-_4JTIOYDuz_2xXu7SwzFiZnwmpde">👉CLICK</a>

## AWS Account Creation <a href ="https://www.youtube.com/watch?v=XhW17g73fvY">👉CLICK</a>

## Django Documentation for CRUD Views <a href="https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/">👉CLICK</a> 


## create and activate environment : 
###### (When anaconda is present)
- `conda create -m myproject python=3.8`
- `activate myproject`
###### (When anaconda is not present) 
- `python3 -m venv myproject`
-  `myproject/Script/activate`

## Install all these packages in environment(myproject) :
- `pip install django`
- `pip install bootstrap` 
- `pip install nltk`
- `pip install newspaper3k`
- `pip install numpy`
- `pip install sklearn`
- `pip install wolframaplha`
- `pip install wikipedia`
- `pip install email`

#### ✋All the steps after this are for those who are creating from stratch not required if you wish to clone this project✋

## Create Django Project :
- `django-admin startproject Myproject`
- `cd Myproject`
- `django-admin startapp Myapp`
- `python3 manage.py runserver`

## Doubts During Meeting :
- <h3>Why we use class based views or when it is the needed to create a class based view rather than defining a function ? </h3>
<p> A view is a callable which takes a request and returns a response. This can be more than just a function, and Django provides an example of some classes which can be used as views. These allow you to structure your views and reuse code by harnessing inheritance and mixins. 
Early on it was recognized that there were common idioms and patterns found in view development. Function-based generic views were introduced to abstract these patterns and ease view development for the common cases.
The problem with function-based generic views is that while they covered the simple cases well, there was no way to extend or customize them beyond some configuration options, limiting their usefulness in many real-world applications.
Class-based generic views were created with the same objective as function-based generic views, to make view development easier. However, the way the solution is implemented, through the use of mixins, provides a toolkit that results in class-based generic views being more extensible and flexible than their function-based counterparts.
Class-based views provide an alternative way to implement views as Python objects instead of functions. They do not replace function-based views, but have certain differences and advantages when compared to function-based views:<br>
- Organization of code related to specific HTTP methods (GET, POST, etc.) can be addressed by separate methods instead of conditional branching.<br>
- Object oriented techniques such as mixins (multiple inheritance) can be used to factor code into reusable components. <p>
  
- <h3>What is purpose of using csrf token ?</h3>
<p> The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries. This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their browser. A related type of attack, ‘login CSRF’, where an attacking site tricks a user’s browser into logging into a site with someone else’s credentials, is also covered.
The first defense against CSRF attacks is to ensure that GET requests (and other ‘safe’ methods, as defined by RFC 7231#section-4.2.1) are side effect free. Requests via ‘unsafe’ methods, such as POST, PUT, and DELETE, can then be protected by following the steps below. </p>

- <h3> What is the use of mixins and decorators also, what is the difference ? </h3>
<p> Decorators add a new functionality to an object without changing other object instances of the same class, while a mixin is a kind of multiple inheritance used to inherit from multiple parent classes. you need mixins when you have a few different classes that should have same functionality.
Good examples of using mixins are Django's class-based views. For example, you have a few different classes: FormView, TemplateView, ListView. All of them have one similar piece of functionality: they have to render templates. Every one of these classes has a mixin, which adds methods required for template rendering.
Another example is if you needed to add a class for an API that returns a JSON result. It could also be inherited from a base, View class. You simply skip template mixins, and define what you need (and probably write your own mixin for JSON encoding).
Additionally, you may override some of methods proposed in mixins which allow you to modify some parts of common code for your local case. It's all about OOP concept. Decorators are used to modify existing functionalities.</p>

<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=letsgetstartedwithbub&theme=chartreuse-dark&show_icons=truelayout=compact&repo=Django_Web_Development" alt="srimathij" /></p>

