from flask import Flask, request, render_template
import urllib as u
import string

app = Flask(__name__)

@app.route('/', methods=['GET'])
def init():
    response = get_quote('TWLO')
    if 0.0 in response[0]:
        return render_template('stock.html', text='Symbol not found!')
    else:
        response = str(response).strip('[]')
        response = response.split(',')
        print "Latest value of " + response[0] + " is" + response[1] + "."
        return render_template('stock.html', text=response[1])

def get_quote(s):
    data = []
    url = 'http://finance.yahoo.com/d/quotes.csv?s='+s
    url += "+&f=sb3b2l1l"
    f = u.urlopen(url,proxies = {})
    rows = f.readlines()
    for r in rows:
        values = [x for x in r.split(',')]
        symbol = values[0][1:-1]
        last = string.atof(values[3])
        data.append([symbol,last])
    return data

if __name__ == "__main__":
    app.run(debug=True, port=5000)
