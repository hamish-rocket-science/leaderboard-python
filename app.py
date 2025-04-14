from flask import Flask, render_template, request, redirect, url_for
from leaderboards import db

app = Flask(__name__)

# PAGES / GET

@app.route("/")
def home():
    scores = db.get_top_scores()
    return render_template("home.html", scores=scores)

@app.route("/leaderboard")
def leaderboard():
    game_mode = request.args.get("game_mode")
    scores = db.get_top_scores(game_mode=game_mode)
    return render_template("leaderboard.html", scores=scores, game_mode=game_mode)

# POST

@app.route("/add_score", methods=["POST"])
def submit_score():
    player_name = request.form.get("player_name")
    score = int(request.form.get("score"))
    game_mode = request.form.get("game_mode")
    db.add_score(player_name, score, game_mode)
    return redirect(url_for("home"))