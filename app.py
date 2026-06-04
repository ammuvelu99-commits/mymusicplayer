from flask import Flask, render_template, jsonify

app = Flask(__name__)

songs = [
    {
        "title": "Song 1",
        "file": "/static/songs/song1.mp3"
    },
    {
        "title": "Song 2",
        "file": "/static/songs/song2.mp3"
    },
    {
        "title": "Song 3",
        "file": "/static/songs/song3.mp3"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/songs")
def get_songs():
    return jsonify(songs)

if __name__ == "__main__":
    app.run(debug=True)