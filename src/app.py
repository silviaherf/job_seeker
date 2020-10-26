from flask import Flask
import src.data_extraction as extract


app = Flask("job_seeker")


@app.route('/')
def hello():
    cover = open('src/html/saludo.html', 'r', encoding='utf-8').read() 
    return cover


@app.route('/search')
def jobs_searching():
    extract.jobs_scrapping()

