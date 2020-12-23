from flask import Flask,request
import src.data_extraction as extract
from src.data_extraction import Linkedin


app = Flask("job_seeker")


@app.route('/')
def hello():
    cover = open('src/html/saludo.html', 'r', encoding='utf-8').read() 
    return cover


@app.route('/search')
def jobs_searching():
    
    buscar=Linkedin()
    buscar.jobs_scrapping('data','Madrid')
    buscar.apply()

