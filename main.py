import requests
import json
from flask import Flask, render_template, url_for, request


app = Flask(__name__, template_folder='templates')
data = requests.get('https://dekontaminasi.com/api/id/covid19/hospitals').json()

prov = []
for i in data:
    prov.append(i['province'])

@app.route('/')
def home():
    return render_template('homepages.html', rs = data, judul = 'Home')

@app.route('/cari', methods = ['POST', 'GET'])
def cari():
    if request.method == 'POST':
        cari = request.form['cari']
        new_list = list(filter(lambda x: (x['province'] == cari), data))
        return render_template('cari.html', rs = new_list, judul='Cari Data')
    else:
        cari = request.args.get('cari')
        return render_template('cari.html')
    
@app.route('/cari-data/')
def caridata():
    q = set(prov)
    p = list(map(lambda x: 'Provinsi ' + x, sorted(q)))
    return render_template('homecari.html', x=p, judul='Cari Data')

@app.route('/about')
def about():
    return render_template('about.html', judul = 'About')

if __name__ == '__main__':
    app.run(debug=True)