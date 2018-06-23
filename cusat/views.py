# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from lib import webSupport
from .forms import NameForm
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            mRollNo=request.POST.get("name")
            mWeb = webSupport.webData1()
            result1=mWeb.getData(mRollNo)
            result1 = mWeb.parse()
            mWeb = webSupport.webData2()
            result2=mWeb.getData(mRollNo)
            result2 = mWeb.parse()
            mWeb = webSupport.webData3()
            result3=mWeb.getData(mRollNo)
            result3 = mWeb.parse()
            mWeb = webSupport.webData4()
            result4=mWeb.getData(mRollNo)
            result4 = mWeb.parse()
            mWeb = webSupport.webData5()
            result5=mWeb.getData(mRollNo)
            result5= mWeb.parse()
            mWeb = webSupport.webData6()
            result6=mWeb.getData(mRollNo)
            result6 = mWeb.parse()
            mWeb = webSupport.webData7()
            result7=mWeb.getData(mRollNo)
            result7= mWeb.parse()
            result8=result2+result3+result4+result5+result6+result7
            result8=result8.replace('''<center>
<img src="http://exam.cusat.ac.in/CUSAT-RESULT/Bresult/logog" width=5% >
<h1>Cochin University of Science and Technology</h1></center>

<div style=text-align:center;>
<h3>GRADE CARD</h3>
</div>
'''," ");
            result =result1+result8
            result=result.replace('''<p>
Note: The Marks / Grades shown in this sheet for a Subject is the Total of Internal and External components of Marks secured. If a Student is absent for one component, Total Marks shown is the other component only.
</p><br>
<p>
Disclaimer: The results published in the site are for immediate information to the examinees. 
This cannot be treated as original marksheet. CUSAT is not responsible for any inadvertant error that may have crept in the results published in the site.
 Original mark sheets will be issued by the Controller of Examinations.
</p><br>


</body>
</html>
'''," ");
            print result
            return HttpResponse(result)



    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def index(request):
	mRollNo = 12151008
	mWeb = webSupport.webData1()
	result1=mWeb.getData(mRollNo)
	result1 = mWeb.parse()
	mWeb = webSupport.webData2()		
	result2=mWeb.getData(mRollNo)			
	result2 = mWeb.parse()
	mWeb = webSupport.webData3()		
	result3=mWeb.getData(mRollNo)			
	result3 = mWeb.parse()
	mWeb = webSupport.webData4()		
	result4=mWeb.getData(mRollNo)			
	result4 = mWeb.parse()
	mWeb = webSupport.webData5()		
	result5=mWeb.getData(mRollNo)			
	result5= mWeb.parse()
	mWeb = webSupport.webData6()		
	result6=mWeb.getData(mRollNo)			
	result6 = mWeb.parse()
	mWeb = webSupport.webData7()		
	result7=mWeb.getData(mRollNo)			
	result7= mWeb.parse()
	result8=result2+result3+result4+result5+result6+result7
	result8=result8.replace('''<center>
<img src="http://exam.cusat.ac.in/CUSAT-RESULT/Bresult/logog" width=5% >
<h1>Cochin University of Science and Technology</h1></center>

<div style=text-align:center;>
<h3>GRADE CARD</h3>
</div>
'''," ");
	result =result1+result8
	result=result.replace('''<p>
Note: The Marks / Grades shown in this sheet for a Subject is the Total of Internal and External components of Marks secured. If a Student is absent for one component, Total Marks shown is the other component only.
</p><br>
<p>
Disclaimer: The results published in the site are for immediate information to the examinees. 
This cannot be treated as original marksheet. CUSAT is not responsible for any inadvertant error that may have crept in the results published in the site.
 Original mark sheets will be issued by the Controller of Examinations.
</p><br>


</body>
</html>
'''," ");
	print result			
	return HttpResponse(result)

