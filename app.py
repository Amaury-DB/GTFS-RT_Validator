from flask import Flask, render_template, request, jsonify
import gtfs_realtime_pb2
import validators
import urllib.request

app = Flask(__name__)

def validate_gtfs_rt(url):
    # Vérifier si l'URL est valide
    if not validators.url(url):
        return {"status": "error", "message": "Invalid URL."}

    # Essayer de télécharger le fichier GTFS-RT
    try:
        response = urllib.request.urlopen(url)
        feed_data = response.read()
    except Exception as e:
        return {"status": "error", "message": f"Error fetching URL: {str(e)}"}

    # Essayer de parser le fichier GTFS-RT
    feed = gtfs_realtime_pb2.FeedMessage()
    try:
        feed.ParseFromString(feed_data)
    except Exception as e:
        return {"status": "error", "message": f"Error parsing GTFS-RT data: {str(e)}"}

    # Si tout est valide
    return {"status": "success", "message": "GTFS-RT feed is valid."}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    url = request.form['url']
    result = validate_gtfs_rt(url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
