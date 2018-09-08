from flask import Flask, render_template

app = Flask(__name__)

# show name method
@app.route('/pokemon/<int:p_dex_num>')

# show pokedex number method
@app.route('/pokemon/<id>')

# main method
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
