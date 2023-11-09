from flask import Flask, render_template, url_for, redirect
import sqlite3
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/alphabet-arabe")
def alphabet():
    try:
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        res = cursor.execute("SELECT * FROM alphabe622").fetchall()
        return render_template('alphabet.html', r=res)
    except Exception:
        print('error')
    finally:
        connect.close()
    return render_template('alphabet.html')

@app.route("/quran")
def coranpage():
    try:
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        res = cursor.execute('SELECT * FROM quransouh').fetchall()
        return render_template('souh.html', r=res)
    except Exception as e:
        print(e)
    finally:
        connect.close()

@app.route("/quran/<id>")
def coranpages(id):
    try:
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        res = cursor.execute('SELECT * FROM quransouh WHERE number = ?', (id,)).fetchone()
        restr = res[2].split('/')
        resar = res[3].split('/')
        resfr = res[4].split('/')
        print(resfr,resar,restr)
        return render_template('souhpage.html', restr=restr,resar=resar,resfr=resfr, souh=res)
    except Exception as e:
        print(e)
    finally:
        connect.close()


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")