from urllib2 import urlopen
import json 

def current(city, state):
	f = urlopen('http://api.wunderground.com/api/fbec2cc984499b31/geolookup/conditions/q/%s/%s.json' % (state, city)) 
	json_string = f.read() 
	parsed_json = json.loads(json_string) 
	temp_f = parsed_json['current_observation']['temp_f'] 

	print "Current temperature in %s, %s is: %s" % (city, state, temp_f) 
	f.close()

def forecast10(city, state):	#10-day forecast (starting today)for given city, state
	f = urlopen('http://api.wunderground.com/api/fbec2cc984499b31/forecast10day/q/%s/%s.json' % (state, city)) 
	json_string = f.read() 
	parsed_json = json.loads(json_string) 
	tenDayList=parsed_json['forecast']['simpleforecast']['forecastday'] 
	high_list=[]
	low_list=[]
	for i in range(len(tenDayList)):
		high_list.append(int(tenDayList[i]['high']['fahrenheit']))
		low_list.append(int(tenDayList[i]['low']['fahrenheit']))
	avg_high = sum(high_list)/len(high_list)
	avg_low = sum(low_list)/len(low_list) 
	return {"avgHigh":avg_high,
			"avgLow": avg_low}
	f.close()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()