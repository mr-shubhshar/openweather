from sys import argv
from sys import exit
import json
import requests as req
from pprint import pprint

scr, city = argv[0], argv[1:]

if len(argv) < 2:
	exit('Usage: weather.py <city_name>')

if city[0] == 'detailed':
	res = req.get('http://api.openweathermap.org/data/2.5/forecast?q=%s&mode=json&appid=4e7ffff527ffe7b280be8d940d744f27' %city[1:])
	try:
		res.raise_for_status()
	except Exception as e:
		print "Something went wrong. That's all I know! %s" %e

	# print res.text

	weather_data = json.loads(res.text)

	# pprint(weather_data)

	report_list = weather_data['list']

	print "The detailed weather report for %s: \n" %((' '.join(city[1:])).title())
	for i in range(3):
		if i == 0:
			print "Today: "
		elif i == 1:
			print "\nTomorrow: "
		else:
			print "\nDay after Tomorrow"

		print 'Humidity' + ' - ' + str(report_list[i]['main']['humidity'])
		print 'Maximum Temperature' + ' - ' + str(report_list[i]['main']['temp_max'])
		print 'Minimum Temperature' + ' - ' + str(report_list[i]['main']['temp_min'])
		print 'Wind' + ' - ' + str(report_list[i]['wind']['speed']) + 'kmph'
		print str(report_list[i]['weather'][0]['main']) + ' - ' + str(report_list[i]['weather'][0]['description'])

else:
	res = req.get('http://api.openweathermap.org/data/2.5/forecast?q=%s&mode=json&appid=4e7ffff527ffe7b280be8d940d744f27' %city)
	try:
		res.raise_for_status()
	except Exception as e:
		print "Something went wrong. That's all I know! %s" %e

	# print res.text

	weather_data = json.loads(res.text)

	# pprint(weather_data)

	report_list = weather_data['list']

	print "Brief weather report for %s: \n" %((' '.join(city)).title())

	print "Today: ",
	print report_list[0]['weather'][0]['description']
	print "Tomorrow: ",
	print report_list[1]['weather'][0]['description']
	print "Day after tomorrow: ",
	print report_list[2]['weather'][0]['description']
