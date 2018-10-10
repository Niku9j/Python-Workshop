from django.http import HttpResponse
from django.template import engines
from django.template.loader import render_to_string
def home(request):
	return HttpResponse("<center><h1>Hello - Home Page</h1></center><br><center>Welcome</center>")

def home1(request):
   title='python workshop Day1 Django - html1 at MMS'
   author='raj'
   about_template = '''
    <html>
    <head>
      <title>Home Page</title>
    </head>
    <body>
        <center><h1>ABOUT ''' + title + '''</h1></center>
        <center><p>Welcome to the <font color=red>First Page</font> in HTML</p></center>
<center><table border=2 bgcolor=yellow>
<tr><th>Roll</th><th>Name</th><th>Age</th></tr>
<tr><td>1</td><td>Akashdeep</td><td>15</td></tr>
<tr><td>2</td><td>Naveen</td><td>17</td></tr>
</table>
        <center><p><h1>Thank You</h1></center>
        <center><p><a href="{% url 'spage' %}">second html page</a>.</p></center>
    </body>
    </html>'''

   django_engine = engines['django']
   template = django_engine.from_string(about_template)
   html = template.render({'title1': title, 'author': author})
   return HttpResponse(html)

def home2(request):
   title='python workshop Day 2  Django - html2 at MMS'
   author='raj'
   about_template = '''<html>
    <html>
    <head>
      <title>Home Page</title>
    </head>
    <body>
        <center><h1>ABOUT ''' + title + '''</h1></center>
        <center><p>Welcome to the <font color=red>Second Page</font> in HTML</p></center>
<center><table border=2 bgcolor=yellow>
<tr><th>Roll</th><th>Bhawna</th><th>Age</th></tr>
<tr><td>1</td><td>Vaishali</td><td>15</td></tr>
<tr><td>2</td><td>Sheetal</td><td>17</td></tr>
</table>
        <center><p><h1>Thank You</h1></center>
        <center><p><a href="{% url 'fpage' %}">first html page</a>.</p></center>
    </body>
    </html>'''

   django_engine = engines['django']
   template = django_engine.from_string(about_template)
   html = template.render({'title1': title, 'author': author})
   return HttpResponse(html)


def home3(request):
   title='python workshop Day2 Django-form at MMS'
   author='raj'
   about_template = '''
    <html>
    <head>
      <title>Home Page</title>
    </head>
    <body>
        <center><h1>ABOUT ''' + title + '''</h1></center>
        <center><p>Welcome to the <font color=red>Authentication Form Page</font> in HTML</p></center>
	<center><form name="auth" action="check_pass" method="get">
	Enter your userid
	<input name="uid" type="text" value=""><br><br>
	Enter your password
	<input name="pwd" type="password" value=""><br><br>
	<input name="sbmt" type="submit" value="submit">
	<input name="sst" type="reset" value="reset">
	</center>
	</form></center>


        <center><p><h1>Thank You</h1></center>
    </body>
    </html>'''

   django_engine = engines['django']
   template = django_engine.from_string(about_template)
   html = template.render({'title1': title, 'author': author})
   return HttpResponse(html)

def check_pass(request):
    ud = request.GET.get('uid') 
    pd = request.GET.get('pwd')
    if pd=="rana9999": 
      about_template = '''
      <html>
	    <head>
	      <title>Checking Page</title>
	    </head>
	    <body>
	       
	        <center><p>Userid and password doisplayed</p></center>
		<br><br><br>
		<center><h1>UId: = <font color=red>'''+ud+'''</font> and PWD: = <font 	color=blue>'''+pd+'''</h1></center>
	        	<center><h1><font color=green><a href="{% url 'homepage' %}">Home page</a></font><h1></center>
	    </body>
      </html>'''
	

      django_engine = engines['django']
      template = django_engine.from_string(about_template)
      html = template.render()
      return HttpResponse(html)
    else:
      return HttpResponse("Better Luck Next Time,......BYE")

def home4(request):
   title='python workshop Day2- Django (processing) at MMS'
   author='raj'
   about_template = '''
    <html>
    <head>
      <title>Calculation Form</title>
    </head>
    <body>
        <center><h1>ABOUT ''' + title + '''</h1></center>
        <center><p>Welcome to the <font color=red>Data Processing  Form Page</font> in HTML</p></center>
<center>
	<form name="cal" action="calculate" method="get">
	Enter the first value
	<input name="val1" type="text" value=""><br>
	Enter the second value
	<input name="val2" type="text" value=""><br>
	<input name="sbmt" type="submit" value="submit">
	<input name="sst" type="reset" value="reset">
	</form>
	</center>

        <center><p><a href="{% url 'homepage' %}">Return to the homepage</a>.</p></center>
	

        <center><p><h1>Thank You</h1></center>
    </body>
    </html>'''

   django_engine = engines['django']
   template = django_engine.from_string(about_template)
   html = template.render()
   return HttpResponse(html)


def calculate(request):
    title = 'cal v1.0'
    author ='raj kumar pal'
    val1 = int(request.GET.get('val1')) 
    val2 = int(request.GET.get('val2'))
    sum=val1+val2  
    about_template = '''
    <html>
    <head>
      <title>''' + title + '''</title>
    </head>
    <body>
        <center><h1>About ''' + title + '''</h1></center>
        <center><p>The sum is ''' + str(sum) + '''</p></center>
        <center><p><a href="{% url 'homepage' %}">Return to the homepage</a>.</p></center>
    </body>
    </html>'''

    django_engine = engines['django']
    template = django_engine.from_string(about_template)
    html = template.render({'title': title, 'author': author})
    return HttpResponse(html)

