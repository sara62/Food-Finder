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
        print item['name']
        print "\n"
        restaurant_list.update(
                    {
                        'name': name.append(item['name']),
                        'link': link.append(item['url']),
                        'is_open': is_open.append(item['is_closed'])
                    }
            )
    print restaurant_list['name']
    return render_template('search.html', term = term, location = location,
                restaurant_list = restaurant_list)
