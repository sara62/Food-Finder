from app import app
from app import searchrequest
from flask import render_template, redirect
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    term = request.form['Search']
    location = request.form['Location']
    requests = searchrequest.search(term, location)
    restaurant_list = {}
    name = []
    link = []
    is_open = []
    for item in requests.values()[2]:
        for index in range(len(requests.values(2))):
            restaurant_list.update(
                    {
                        'name': name.append(item.values()[5]),
                        'link': link.append(item.values()[7]),
                        'is_open': is_open.append(item.values()[8])
                    }
            )
    print restaurant_list
    return render_template('search.html', term = term, location = location,
                restaurant_list = restaurant_list)
