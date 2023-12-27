
from flask import Flask, render_template, request, g
import sqlite3

from config import Config
from FDataBase import FDataBase



app = Flask(__name__)
app.config.from_object(Config)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True



def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn



def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()



def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db



@app.route('/', methods=['POST', 'GET'])
def view():
    db = get_db()
    dbase = FDataBase(db)
    configs = sorted(dbase.read_conf(), key=lambda x: x.revision, reverse=True)
    conf = configs[0].configuration  

    if request.method == 'POST':
        version = request.form.get('v1')
        conf = dbase.get_conf(version)['config']
        return render_template('view.html', configs=configs, content=conf)    
    return render_template('view.html', configs=configs, content=conf)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)