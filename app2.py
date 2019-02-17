# import necessary libraries
import requests
import pymongo
from config import NEWS_KEY
#from countries import countries, country_codes
from flask import Flask, jsonify, render_template
# #################################################
# # Flask Setup
# #################################################
# app.config["MONGO_URI"] = "mongodb://localhost:27017/news_app"
app = Flask(__name__)

# # Or set inline
# # mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def map():
    return render_template("index.html")

# @app.route("/mapdata")
# def mapdata():
    
# @app.route("/createdb")
# def update():
#     news = mongo.db.news.find_one()
#     return render_template("index.html", news=news)
#     news.update({}, news_data, upsert=True)
#     return "Creation Successful!"

# @app.route("/dash")
# def dash():

# @app.route("/dashdata")
# def dashdata():
#     stmt = db.session.query(country_data).statement
#     df = pd.read_sql_query(stmt, db.session.bind)
#     # Filter the data based on the sample number and
#     # only keep rows with values above 1
#     country_data = df.loc[df[country_data] > 1, ["name", "keyword", country_data]]
#     # Format the data to send as json
#     data = {
#         "name": country_data.name.values.tolist(),
#         "keyword": country_data[keywords].values.tolist(),
#         "": country_data..tolist(),
#     }
#     return jsonify(data)

# @app.route("/update")
# def update():

if __name__ == "__main__":
    #easy port change
    app.run(host='0.0.0.0', port=9999, debug=True)