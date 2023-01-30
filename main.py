import requests
import json
from flask import Flask, render_template, url_for, request


app = Flask(__name__, template_folder='templates')
data = requests.get('https://indonesia-public-static-api.vercel.app/api/heroes').json()

name = []
for i in data:
    name.append(i['name'])

@app.route('/')
def home():
    return render_template('homepages.html', phlwn = data, judul = 'Home')

@app.route('/cari', methods = ['POST', 'GET'])
def cari():
    if request.method == 'POST':
        cari = request.form['cari']
        new_list = list(filter(lambda x: (x['name'] == cari), data))
        return render_template('cari.html', phlwn = new_list, judul='Cari Data')
    else:
        cari = request.args.get('cari')
        return render_template('cari.html')
    
@app.route('/cari-data/')
def caridata():
    q = set(name)
    p = list(map(lambda x: x, sorted(q)))
    return render_template('homecari.html', x=p, judul='Cari Data')

@app.route('/about')
def about():
    return render_template('about.html', judul = 'About')

if __name__ == '__main__':
    app.run(debug=True)