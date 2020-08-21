from flask import Flask, render_template, request
from api import apiKey
import requests

app = Flask(__name__)
steamID = '76561197960434622'
url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={apiKey}&steamid={steamID}'
rGames = requests.get(url)


@app.route('/', methods=['POSt', 'GET'])
def index():
    if request.method == 'POST':
        games = {}
        for i in rGames.json()['response']['rGames']:
            games[rGames.json()['appid']] = 
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
