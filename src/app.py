from flask import Flask,request
import src.data_extraction as extract
from src.data_extraction import Linkedin


app = Flask("job_seeker")


@app.route('/')
def hello():
    cover = open('src/html/saludo.html', 'r', encoding='utf-8').read() 
    return cover


@app.route('/search',methods=['GET', 'POST'])
def jobs_searching():
   
    buscar=Linkedin()
    if request.method == 'POST':
        keyword=request.form.get("keyword")
        location=request.form.get("location")


    else:
        keyword=request.args.get("keyword")
        location=request.args.get("location")

    buscar.jobs(keyword,location)
    buscar.filters()
    buscar.more_jobs()
    buscar.apply()

