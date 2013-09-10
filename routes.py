from flask import Flask, render_template, request, url_for, flash, redirect, g, _app_ctx_stack, send_from_directory
from shop_style import *
from model import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def landing_page():
	return render_template('landing_page.html')

@app.route('/homepage', methods=['GET', 'POST'])
def home_page():
	person = request.args['person']
	date = request.args['date']
	location = request.args['location']
	place = location.split(", ")
	city = str(place[0])
	print "THE city", city
	state = str(place[1])
	
	avgTempDict = forecast10(city, state)

	avgHigh = avgTempDict["avgHigh"]
	
	show_these = which_products(person, avgHigh)

	return render_template('home_page.html',
		person=person,
		date=date,
		city = city,
		state = state,
		tops=show_these[0],
		bottoms = show_these[1],
		frosting = show_these[2],
		avgHigh = avgHigh
		)

if __name__ == '__main__':
    app.run(debug=True)