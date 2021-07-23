import os
import http.client
import json
import urllib.parse
import webbrowser
import requests
import html.parser


from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash




app = Flask(__name__)



app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/airports", methods=["GET","POST"])
def airports():
     if request.method == "POST":
         conn = http.client.HTTPSConnection("airport-info.p.rapidapi.com")

         headers = {
               'x-rapidapi-key': "631886454bmshcbf6a635b2cd1c7p17022bjsnb381f40641e2",
               'x-rapidapi-host': "airport-info.p.rapidapi.com"
               }

         #airport = input("Airport:")
         airport = (request.form.get("airport"))
         conn.request("GET", "/airport?iata={}".format(airport), headers=headers)

         res = conn.getresponse()
         data = res.read()

         #response = data.decode("utf-8")

         #quote = data.json()

         jsonResponse = json.loads(data.decode('utf-8'))



         print(jsonResponse)

         return render_template("airportfound.html", data=jsonResponse)



     else:


         return render_template("airports.html")

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/flightsearch", methods=["GET","POST"])
def flightsearch():
    if request.method == "POST":


        departureairport = (request.form.get("departureairport"))
        destinationairport = (request.form.get("destinationairport"))
        departuredate = (request.form.get("departuredate"))
        returndate = (request.form.get("returndate"))





        link = ("https://www.skyscanner.net/transport/flights/{}/{}/{}/{}/".format(departureairport,destinationairport,departuredate,returndate))
        print(link)

        #return render_template("flightsfound.html", data=jsonResponse)
        return redirect(link)

       # return render_template("flightsfound.html", link=link)
        #return link


    else:
        return render_template("flightsearch.html")


@app.route("/departures", methods=["GET","POST"])
def departures():
    if request.method == "POST":
        airport = (request.form.get("airport"))


        params = {
            'access_key': '48ca22b29805cd249127bf8c7d8fdb08',
            'dep_iata': format(airport),

        }

        api_result = requests.get('http://api.aviationstack.com/v1/flights', params)


        api_response = api_result.json()

        #stream = json.loads(api_response)
        data = api_response["data"]
        info = (json.dumps(data, indent=4, sort_keys=True))

        print(info)

        f = open("static/demofile.txt", "w")
        f.write(info)
        f.close()

        f = open("static/demofile.txt", "r")

      #  flight = client.api_response.find_one({'flight'})





        return render_template("flightsloaded.html")



    else:
        return render_template("departures.html")

@app.route("/arrivals", methods=["GET","POST"])
def arrivals():
    if request.method == "POST":
        airport = (request.form.get("airport"))


        params = {
            'access_key': '48ca22b29805cd249127bf8c7d8fdb08',
            'arr_iata': format(airport),

        }

        api_result = requests.get('http://api.aviationstack.com/v1/flights', params)


        api_response = api_result.json()

        #stream = json.loads(api_response)
        data = api_response["data"]
        info = (json.dumps(data, indent=4, sort_keys=True))

        print(info)

        f = open("static/demofile.txt", "w")
        f.write(info)
        f.close()

        f = open("static/demofile.txt", "r")






        return render_template("flightsloaded.html")



    else:
        return render_template("arrivals.html")


