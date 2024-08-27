from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/', methods=['GET'])
def serve_page():
    return send_from_directory('.', 'forweb.html')


if __name__ == '__main__':
    app.run(debug=True)
