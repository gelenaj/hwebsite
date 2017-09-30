from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask import Flask, request, redirect, render_template, flash
from flask_script import Manager
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask_googlemaps import icons
from flask_assets import Environment, Bundle
import smtplib
import string
from os import environ
import psycopg2
import urllib.parse

app = Flask(__name__, template_folder="templates")
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['GOOGLEMAPS'] = os.environ['GOOGLEMAPS_KEY']

GoogleMaps(app)
db = SQLAlchemy(app)

js = Bundle('js/timeline_show_all.js',
            output='gen/main.js')
assets = Environment(app)
assets.init_app(app)
assets.register('main.js', js)
manager = Manager(app)

from models import *
migrate=Migrate(app, db)

@app.route('/')
def index():
    featuredNews=News.query.filter_by(featured=True)
    return render_template('index.html', featuredNews=featuredNews)


@app.route('/hondurasmap')
def hondurasmap():
    HondurasBases=Map(
        identifier="HondurasBases",
        lat=14.656934,
        lng=-86.556886,
        zoom=7,
        style="height:450px;border:0;allowfullscreen;",
        markers=[
        {
        'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
        'lat':15.5149,
        'lng':-87.9923,
        'infobox':"<p>Soto Cano/Palmerola</p>"
        },
        {
        'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
        'lat':15.039154,
        'lng':-84.275469,
        'infobox':"<p>Mocoron Tropics Region Testing Center</p>"
            },
        {
        'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
        'lat':15.038947,
        'lng':-84.277315,
        'infobox':"<p>Mocoron</p>"
            },
         {
        'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
        'lat':16.443976,
        'lng':-85.902367,
        'infobox':"<p>Guanaja</p>"

            },
        {
        'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
        'lat':16.010554,
        'lng':-85.95134,
        'infobox':"<p>Puerto Castilla</p>"

            },
        {
        'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
        'lat':13.795229,
        'lng':-87.289524,
        'infobox':"<p>La Venta</p>"
        },
        {
        'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
        'lat':13.950329,
        'lng':-87.132217,
        'infobox':"<p>El Aguacate</p>"
        },
         {
        'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
        'lat':15.267511,
        'lng':-83.771347,
        'infobox':"<p>Puerto Lempira</p>"
        },
        {
        'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
        'lat':15.793265,
        'lng':-85.964799,
        'infobox':"<p>La Brea</p>"
        },
        ]
    )
    return render_template('hondurasmap.html',HondurasBases=HondurasBases)


@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/news', methods=['GET'])
def news():
    NewsId=request.args.get('id')

    if NewsId:
        news_entry=News.query.get(NewsId)
        queryAllLinks=Links.query.all()
        allLinks=Links.query.filter_by(owner_links_id=NewsId)
        return render_template('newsentry.html', news_entry=news_entry, allLinks=allLinks)

    news_story = News.query.all()
    return render_template('news.html', news_story=news_story)

if __name__ == '__main__':
    app.run(debug=True)
