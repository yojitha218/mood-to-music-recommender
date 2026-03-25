from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "AIzaSyAW6sWINnrP2dg3eXTjHgVAvm6AY5yW50M"


def get_songs(mood, language):

    query = f"{language} {mood} songs"

    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&maxResults=12&key={API_KEY}"

    response = requests.get(url).json()

    songs = []

    for item in response.get('items', []):
        video_id = item['id'].get('videoId')

        if not video_id:
            continue

        songs.append({
            "title": item['snippet']['title'],
            "thumbnail": item['snippet']['thumbnails']['high']['url'],
            "video": f"https://www.youtube.com/embed/{video_id}"
        })

    return songs


@app.route('/')
def home():
    return render_template("index.html", songs=None)


@app.route('/submit', methods=['POST'])
def submit():
    mood = request.form.get('mood')
    language = request.form.get('language')

    songs = get_songs(mood, language)

    return render_template("index.html", songs=songs, mood=mood)


if __name__ == '__main__':
    app.run(debug=True)