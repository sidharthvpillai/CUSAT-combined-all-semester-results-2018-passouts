# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import itertools
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from lib import webSupport
from .forms import NameForm
def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            a=[
            ['May','2015','1&2','Regular'],
            ['May','2015','1&2','Revaluation'],
            ['June','2016','1&2','Improvement'],
            ['June','2016','1&2','Supplementary'],
            ['June','2016','1&2','Revaluation'],
            ['June','2017','1&2','Improvement'],
            ['June','2017','1&2','Supplementary'],
            ['June','2017','1&2','Revaluation'],
            ['November','2015','3','Regular'],
            ['November','2015','3','Revaluation'],
            ['November','2016','3','Improvement'],
            ['November','2016','3','Supplementary'],
            ['November','2016','3','Revaluation'],
            ['November','2017','3','Improvement'],
            ['November','2017','3','Supplementary'],
            ['November','2017','3','Revaluation'],
            ['April','2016','4','Regular'],
            ['April','2016','4','Revaluation'],
            ['March','2017','4','Improvement'],
            ['March','2017','4','Supplementary'],
            ['March','2017','4','Revaluation'],
            ['June','2017','4','Improvement'],
            ['June','2017','4','Supplementary'],
            ['June','2017','4','Revaluation'],
            ['November','2016','5','Regular'],
            ['November','2016','5','Revaluation'],
            ['May','2017','5','Improvement'],
            ['May','2017','5','Supplementary'],
            ['May','2017','5','Revaluation'],
            ['November','2017','5','Improvement'],
            ['November','2017','5','Supplementary'],
            ['November','2017','5','Revaluation'],
            ['April','2017','6','Regular'],
            ['April','2017','6','Revaluation'],
            ['April','2018','6','Improvement'],
            ['April','2018','6','Supplementary'],
            ['April','2018','6','Revaluation'],
            ['November','2017','7','Regular'],
            ['November','2017','7','Revaluation'],
            ['April','2018','7','Improvement'],
            ['April','2018','7','Supplementary'],
            ['April','2018','7','Revaluation'],
            ['April','2018','8','Regular'],
            ['April','2018','8','Revaluation'],
            ]
            mRollNo=request.POST.get("name")
            result1 = ''''''
            for i in  a:
            	#print i
            	mWeb = webSupport.webData(i)
                result=mWeb.getData(mRollNo)
            	result = mWeb.parse()
            	result1=result1+result
            	#print result1
            result1=result1.replace('''<p>
Note: The Marks / Grades shown in this sheet for a Subject is the Total of Internal and External components of Marks secured. If a Student is absent for one component, Total Marks shown is the other component only.
</p><br>
<p>
Disclaimer: The results published in the site are for immediate information to the examinees. 
This cannot be treated as original marksheet. CUSAT is not responsible for any inadvertant error that may have crept in the results published in the site.
 Original mark sheets will be issued by the Controller of Examinations.
</p><br>
''',"")
            result1=result1.replace('''</body>
</html>
<html>
<head>
<body bgcolor="#CEF6EC">

<center>
<img src="http://exam.cusat.ac.in/CUSAT-RESULT/Bresult/logog" width=5% >
<h1>Cochin University of Science and Technology</h1></center>

<div style=text-align:center;>
<h3>GRADE CARD</h3>
</div>




<table width="100%" class="order-list" border="2">
<tr>
<td><b>Subject Code</b></td>
<td><b>Subject Name</b></td>
<th>Marks (Grade)</th>
<th>Result</th></tr>


</table>
      Total : <br>
      GPA   : <br>
''',"")
            result1=result1.replace('''<html>
<head>
<body bgcolor="#CEF6EC">

<center>
<img src="http://exam.cusat.ac.in/CUSAT-RESULT/Bresult/logog" width=5% >
<h1>Cochin University of Science and Technology</h1></center>

<div style=text-align:center;>
<h3>GRADE CARD</h3>
</div>''','')
            result='''<html>
<head>
<body bgcolor="LightGray">

<center>
<img src="http://exam.cusat.ac.in/CUSAT-RESULT/Bresult/logog" width=5% >
<h1>Cochin University of Science and Technology</h1></center>

<div style=text-align:center;>
<h3>GRADE CARD</h3>
</div>'''+result1

            result=result.replace('''<p align=center><font size=4 >
            <b>CGPA&nbsp;:&nbsp;8.3</b><br>

            <b>Classification&nbsp;:&nbsp;First Class With Distinction</b><br>
            </font></p>
          

    










     
                    <p align=center><font size=4 >
            <b>CGPA&nbsp;:&nbsp;8.3</b><br>

            <b>Classification&nbsp;:&nbsp;First Class With Distinction</b><br>
            </font></p>''','''<p align=center><font size=4 >
            <b>CGPA&nbsp;:&nbsp;8.3</b><br>

            <b>Classification&nbsp;:&nbsp;First Class With Distinction</b><br>
            </font></p>''')
            print result
            return HttpResponse(result)


#            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

