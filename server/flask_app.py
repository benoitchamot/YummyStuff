run_local = True

if run_local:
	DB_PATH = 'votes_db.sqlite'
else:
	DB_PATH = 'votes_db.sqlite'
	
#########################################################
# Dependencies
#########################################################
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from pathlib import Path

# CORS
from flask_cors import CORS

# Local modules


# Ignore warnings
import warnings
warnings.simplefilter(action='ignore')

#########################################################
# Database Setup
#########################################################

# Create engine to movies_db.sqlite
print("Connecting to database...")
db_path = Path(DB_PATH)
engine = create_engine(f"sqlite:///{db_path}")
print("Connected.")

# Reflect the database into a new model
print("Reflecting database...")
Base = automap_base()
print("Done.")

# Reflect the tables
print("Reflecting tables...")
try:
	Base.prepare(engine, reflect=True)
	print("Done.")
except Exception as inst:
    print(f"\nError: {inst}")
    print("\n*** HINT: please run script from within Server directory ***\n")
    quit()

# Save references to each table
Votes = Base.classes.votes

#########################################################
# Flask Setup
#########################################################
app = Flask(__name__)
CORS(app)

#########################################################
# Flask Static Routes
#########################################################

# Default route
@app.route("/")
def home():
	print("Server received request for Home page")
	return (
		f"<h1>YummyStuff API</h1>"
		f"<h2>Static routes</h2>"
		f"<p><a href='api/v1.0/vote'>/api/v1.0/vote</a></p>"
		f"<ul>"
		f"	<li>Vote for a selected recipe</li>"
		f"</ul>"
	)

# Dynamic voting route
@app.route("/api/v1.0/vote/r/<recipe>/n/<name>")
def api_movies_by_actor_and_genre(recipe, name):
	# TODO: register vote in database
    print("Server received request to vote")
	
    # Open session to the database
    session = Session(bind=engine)

    # Add data to database
    session.add(Votes(
        #vote_id = ...
        date = dt.datetime.now(),
        voter_name = name,
        recipe = recipe
    ))
	
    session.commit()

    # Close session
    session.close()

    return jsonify({"Success": f"{name} added one vote for {recipe}."}) 

if run_local:
	#########################################################
	# Run App
	#########################################################
	if __name__ == "__main__":
		app.run(debug=True)
		
