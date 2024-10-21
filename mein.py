from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
      return render_template('index.html')

@app.route('/orcamento', methods=['GET', 'POST'])
def orcamento():
      return render_template('orc_index.html')


if __name__ == '__main__': 
      app.run(debug=True)

