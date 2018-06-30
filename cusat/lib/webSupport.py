import urllib2,urllib
import re
import datetime


class webData():
	
	def __init__(self,i):
		self.__body = ""
		self.__month = i[0]
		self.__year = i[1]
		self.__sem = i[2]
		self.__res_type = i[3]
		self.__time = datetime.datetime.strftime(datetime.datetime.now(),"%Y/%m/%d+%H:%M:%S.000+GMT+0530")
	def getData(self,regn,url='http://exam.cusat.ac.in/erp5/cusat/CUSAT-RESULT/Result_Declaration/display_sup_result'):
		"GET DATA FROM URL"

		data = urllib.urlencode({		# SET OF POST VALUES THAT HAVE TO BE TRANSFERED TO SERVER.
		'regno'		:regn,
		'date_time'	:self.__time,
		'ipadress'	:"",
		'month'		:self.__month,
		'year'		:self.__year,
		'semester'	:self.__sem,
		'result_type'	:self.__res_type,
		'deg_name'	:'B.Tech',
		'statuscheck'	:'failed'})

		websrc = urllib2.urlopen(url,data)
		self.__body = websrc.read()

	def setMonth(self,m) : self.__month=m		# set Month of Exam [ eg : webData.setMonth('April')]
	def setYear(self,m) : self.__year=m		# Set Year of Exam [ eg : webData.setMonth('2017')]
	def setSem(self,m) : self.__sem=m		# Set Semester of Exam [eg : webData.setMonth('8')]
	def setResultType(self,m) : self.__res_type=m	# Set Resutl type Regular / Improvement / Supplimentary
							# 			[ eg: webData.setResultType('Regular') ]


	def parse(self):				# RETURNS A ',' SEPERATED FILES
		"PARSE DATA FROM GETDATA METHOD AND RETURNS A ',' SEPERATED FILES"
		text = self.__body					
		if re.search("Invalid Registration number",text): 
			return "RollNumber Not Found"
		return text
