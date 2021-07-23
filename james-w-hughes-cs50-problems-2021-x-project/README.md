# Flight//Plan
#### Video Demo: https://youtu.be/FKxstW1RycU
#### Description:
This is a simple website where you can look up airports,
flight prices, arrivals and departures.
Use the headings at the top of the page depending
on what you want to do. The website uses
flask (python), HTML (bootstrap) and two APIs
(airport-info.p.rapidapi.com) and (api.aviationstack.com/v1/flights)
to provide the relevant data, as well as
a link to SkyScanner through a form and hyperlink.

Below are descriptions of each of the files used within the project:

# application.py

The overall flask application which runs the website,
with subsections for rendering each page.
Different tasks are done depending on "GET" or "POST",
as the next stage can only happen after the user has filled the form out.

# templates:
# airportfound.html

This returns the airport and a hyperlink to its website
after the user has requested it, through the (airport-info.p.rapidapi.com) API.

# airports.html

The user can search for the airport of his choice from IATA
code here, and then be redirected to airportfound.html to see the results.

# arrivals.html

Look up the latest arrivals through an API at any airport.
The data is downloaded from the aviationstack API into a txt file, which can then
be displayed back to the user on the following page.

# departures.html

Look up the latest departures through an API at any airport.
The data is downloaded from the aviationstack API into a txt file, which can then
be displayed back to the user on the following page.

# flightsearch.html

Look up the latest flight prices for a route on a date
(return optional), linked to Skyscanner's search engine.
The results are formed by adding the contents of the form
to SkyScanner's url.

# flightsloaded.html

Displays the arrival or departure data from the API (pretty printed so the user can read it),
by loading a txt file. The user can scroll through this like an airport departure board,
for information on the flight (departure, arrival, terminal, time, codeshares).

# index.html

The home or index page of the site, where the user will start. As all pages have a navigation bar
it is not necessary to come back here between tasks, and the user can go from anywhere on the site
to anywhere else with one click.

# navbar-top.css

Part of the website template, sourced from bootstrap.


# static/demofile.txt

API data is stored here, then it can be returned to the user on flightsloaded.html.
This can be constantly overwritten so the user can search for new airports.