from flask import Flask, render_template
import requests
#import json

app = Flask(__name__)

base_url = 'http://pokeapi.co/api/v2/pokemon/'

# show name method
@app.route('/pokemon/<int:pdex>')
def get_name(pdex):
    url = base_url + str(pdex) + '/'
    request = requests.get(url)
    name = request.json()['name']
    return 'The pokemon with id %d is %s' % (pdex, name)

# show pokedex number method
@app.route('/pokemon/<name>')
def get_pdex(name):
    url = base_url + name + '/'
    request = requests.get(url)
    pdex = request.json()['id']
    return '%s has id %d' % (name, pdex)

# main method
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
