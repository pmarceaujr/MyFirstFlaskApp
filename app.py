from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

# app.config.update(
#     SECRET_KEY='topsecret',
#     SQLALCHEMY_DATABASE_URI='<database>:<user_id>:<password>@<server>/<database_name>',
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
# )

app.config.update(
    SECRET_KEY='password',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:password@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)


@app.before_request
def some_function():
    g.string = '<br> This code ran before any request'


# BASIC ROUTE
@app.route('/index1')
@app.route('/')
def hello_flask():
    return 'Hello Flask! <br>' + g.string


# QUERY STRINGS
@app.route('/new1/')
def query_strings(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is : {0} </h1>'.format(query_val) + g.string


@app.route('/index')
def hello_index():  # put application's code here
    return 'Hello Index!'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/new/')
def query_string():
    query_val = request.args.get('greeting')
    return f'<h1> The greeting is {query_val}'


@app.route('/new_default/')
def query_with_default(greeting='No greeting passed'):
    query_val = request.args.get('greeting', greeting)
    return f'<h1> The greeting is {query_val}'


@app.route('/user/')
@app.route('/user/<name>')
def no_query_strings(name='Jerry'):
    query_val = request.args.get('greeting', name)
    return f'<h1> The greeting is {query_val}'


# Strings
@app.route('/text/<string:some_text>')
def just_strings(some_text):
    return f'<h1> Working with strings: {some_text}'


# Numbers
@app.route('/numbers/<int:some_integer>')
def just_numbers(some_integer):
    return f'<h1> Working with numbers: {some_integer}'


# Floats
@app.route('/floats/<float:some_float>')
def just_floats(some_float):
    return f'<h1> Working with floats: {some_float}'


# Add
@app.route('/add/<int:num1>/<int:num2>')
def just_adding(num1, num2):
    return f'<h1> Adding numbers: {num1} + {num2} =  {num1 + num2}'


# Multiply
@app.route('/multiply/<float:num1>/<float:num2>')
def just_multiply(num1, num2):
    return f'<h1> Multiplying numbers: {num1} * {num2} =  {num1 * num2}'


# Rendering templates
@app.route('/greeting')
def using_templates():
    return render_template('greeting.html')


# JINJA TEMPLATES
@app.route('/watch')
def top_movies():
    movie_list = ['Star Wars - A New Hope',
                  'The Empire Strikes Back',
                  'Return Of The Jedi',
                  'Phantom Menace',
                  'Attack of the Clones',
                  'Revenge of the Sith',
                  'The Force Awakens',
                  'The Last Jedi',
                  'The Rise of Skywalker'
                  ]

    return render_template('movies.html',
                           movies=movie_list,
                           name='JimmyJohn')


# JINJA TEMPLATES 2
@app.route('/tables')
def movies_plus():
    movies_dict = \
        {
            'Star Wars - A New Hope': 'May 25, 1977',
            'The Empire Strikes Back': 'May 21, 1980',
            'Return Of The Jedi': 'May 25, 1983',
            'Phantom Menace': 'May 19, 1999',
            'Attack of the Clones': 'May 16, 2002',
            'Revenge of the Sith': 'May 19, 2005',
            'The Force Awakens': 'December 18, 2015',
            'The Last Jedi': 'December 15, 2017',
            'The Rise of Skywalker': 'December 20, 2019'
        }

    return render_template('movie_table.html',
                           movies=movies_dict,
                           name='JimmyJohn')


# JINJA TEMPLATES WITH CSS
@app.route('/tables_css')
def movies_css():
    movies_dict = \
        {
            'Star Wars - A New Hope': 'May 25, 1977',
            'The Empire Strikes Back': 'May 21, 1980',
            'Return Of The Jedi': 'May 25, 1983',
            'Phantom Menace': 'May 19, 1999',
            'Attack of the Clones': 'May 16, 2002',
            'Revenge of the Sith': 'May 19, 2005',
            'The Force Awakens': 'December 18, 2015',
            'The Last Jedi': 'December 15, 2017',
            'The Rise of Skywalker': 'December 20, 2019'
        }

    return render_template('movies_tables2.html',
                           movies=movies_dict,
                           name='JimmyJohn')


# JINJA2 - FILTERS
@app.route('/filters')
def filter_data():
    movies_dict = \
        {
            'Star Wars - A New Hope': 1977.123,
            'The Empire Strikes Back': 1980.321,
            'Return Of The Jedi': 1983.456,
            'Phantom Menace': 1999.654,
            'Attack of the Clones': 2002.69,
            'Revenge of the Sith': 2005.658,
            'The Force Awakens': 2015.99,
            'The Last Jedi': 2017.885,
            'The Rise of Skywalker': 2019.555
        }

    return render_template('filters.html',
                           movies=movies_dict,
                           name=None,
                           film='a christmas carol')


# JINJA2 - MACROS
@app.route('/macros')
def jinja_macros():
    movies_dict = \
        {
            'Star Wars - A New Hope': 1977.123,
            'The Empire Strikes Back': 1980.321,
            'Return Of The Jedi': 1983.456,
            'Phantom Menace': 1999.654,
            'Attack of the Clones': 2002.69,
            'Revenge of the Sith': 2005.658,
            'The Force Awakens': 2015.99,
            'The Last Jedi': 2017.885,
            'The Rise of Skywalker': 2019.555
        }

    return render_template('using_macros.html', movies=movies_dict)


# SESSION OBJECT
@app.route('/session')
def session_data():
    if 'name' not in session:
        session['name'] = 'Mr Chicken'
    return render_template('session.html', session=session, name=session['name'])


print("Before Table Class")


# PUBLICATION TABLE
class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'The name is is {self.name}'


# BOOK TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # ESTABLISH A RELATIONSHIP BETWEEN PUBLICATION AND BOOK TABLES
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return f'Book title: {self.title} Author:  {self.author}'


with app.app_context():
    print("do db")
    db.create_all()

if __name__ == '__main__':
    print("made it)")
    db.create_all()
    app.run(debug=True)

# To get the creaete_all() to execute do it in terminal in Python console
# >>> from app import app, db
# >>> app.app_context().push()
# >>> db.create_all()

# Or try this in the code:
# with app.app_context():
#     db.create_all()

# To add records from the Python console:
# >>> from app import app, db, Publication, Book
# >>> app.app_context().push()
# >>> pub = Publication(100, "Staples Publishing")
# >>> pub
# The id is 100, Name is is Staples Publishing
# >>> pub2 = Publication(200, "Oxford Publishing")
# >>> pub2
# The id is 200, Name is is Oxford Publishing
# >>> pub.name
# 'Staples Publishing'
# >>> app.app_context().push()
# >>> db.session.add(pub)
# >>> db.session.commit()
# >>> db.session.add(pub2)
# >>> db.session.commit()
# >>> pub3 = Publication(300, "Paramount Press")
# >>> pub4 = Publication(400, "Oracle Press")
# >>> pub5 = Publication(500, "Maple Leaf Publishing")
# >>> db.session.add_all([pub3, pub4, pub5])
# >>> db.session.commit()
# >>> db.session.close()

# >>> dir(Book)
# >>> Book.query.all()
# >>> all = Book.query.all()
# >>> all
# [Book title: Miky's Delivery Service Author:  William Dobelli, Book title: The Secret Life of Walter Kitty Author:  Kitty Stiller, Book title: The Empty Book of Life Author:  Roy Williamson, Book title: Life After Dealth Author:  Nikita Kimmel, Book title: The Legen
# d of Dracula Author:  Charles Rowling, Book title: Taming Dragons Author:  James Vonnegut, Book title: The Singing Magpie Author:  Oscar Steinbeck, Book title: Mr. Incognito Author:  Amelia Funke, Book title: A Dog without purpose Author:  Edgar Dahl, Book title: A
# Frog's Life Author:  Herman Capote, Book title: Logan Returns Author:  Margaret Elliot, Book title: Thieves of Kaalapani Author:  Mohit Gustav, Book title: As Men Thinketh Author:  Edward McPhee, Book title: Mathematics of Music Author:  Mary Turing, Book title: The
#  Mystery of Mandalas Author:  Jack Morrison, Book title: The Sacred Book of Kairo Author:  Heidi Zimmerman, Book title: Love is forever, As Long as it lasts Author:  Kovi O'Hara, Book title: Order in Chaos Author:  Wendy Sherman]
# >>> type(all)
# <class 'list'>
# >>> first = Book.query.first()
# >>> first
# Book title: Miky's Delivery Service Author:  William Dobelli
# >>>
# >>> filter_data = Book.query.filter_by(format='ePub')
# >>> filter_data
# <flask_sqlalchemy.query.Query object at 0x000002212417CFA0>
# >>> filter_data = Book.query.filter_by(format='ePub').all()
# >>> filter_data
# [Book title: Miky's Delivery Service Author:  William Dobelli, Book title: The Sacred Book of Kairo Author:  Heidi Zimmerman]
# >>>
# >>> fancy_data = Book.query.filter_by(format='Paperback').order_by(Book.title).all()
# >>> fancy_data
# [Book title: As Men Thinketh Author:  Edward McPhee, Book title: Life After Dealth Author:  Nikita Kimmel, Book title: The Mystery of Mandalas Author:  Jack Morrison, Book title: Thieves of Kaalapani Author:  Mohit Gustav]
# >>>
# >>> result = Publication.query.filter_by(name='Broadway Press').first()
# >>> result
# The name is is Broadway Press
# >>> result.name
# 'Broadway Press'
# >>> result.id
# # 6
# >>> broadway_books = Book.query.filter_by(pub_id = result.id).all()
# >>> broadway_books
# [Book title: As Men Thinketh Author:  Edward McPhee, Book title: Mathematics of Music Author:  Mary Turing, Book title: The Mystery of Mandalas Author:  Jack Morrison]
# >>>
# >>> u = Book.query.get(34)
# >>> u
# Book title: The Sacred Book of Kairo Author:  Heidi Zimmerman
# >>> u.id
# 34
# >>> u.title
# 'The Sacred Book of Kairo'
# >>> u.format
# 'ePub'
# >>> u.format = 'Hardcover'
# >>> db.session.commit()
# >>> u.format
# 'Hardcover'
# >>> x = Book.query.get(35)
# >>> x
# Book title: Love is forever, As Long as it lasts Author:  Kovi O'Hara
# >>> x.id
# 35
# >>> db.session.delete(x)
# >>> db.session.commit()
# >>>
# >>> Book.query.filter_by(pub_id=6).delete()
# 3
# >>> db.session.commit()
# >>> Publication.query.filter_by(id=6).delete()
# 1
# >>> db.session.commit()
# >>>
