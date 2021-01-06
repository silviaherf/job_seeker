from flask import Flask,request
import src.data_extraction as extract
from src.data_extraction import Linkedin


app = Flask("job_seeker")


@app.route('/')
def hello():
    cover = open('src/html/saludo.html', 'r', encoding='utf-8').read() 
    return cover


@app.route("/search")
def ask_jobs():
    search = open('src/html/buscar.html', 'r', encoding='utf-8').read() 
    return search



@app.route('/search/jobs',methods=['GET', 'POST'])
def jobs_searching():
    buscar=Linkedin()
    if request.method == 'POST':
        keyword=request.form.get("keyword")
        location=request.form.get("location")
        easy_apply=request.form.get("easy_apply")
        remote=request.form.get("remote")


    else:
        keyword=request.args.get("keyword")
        location=request.args.get("location")

    buscar.jobs(keyword=keyword,location=location)
    
    if not easy_apply and remote:
        buscar.filters(remote)
    elif not remote and easy_apply:
        buscar.filters(easy_apply)
    elif not remote and not easy_apply:
        buscar.filters()
    else:
        buscar.filters(easy_apply,remote)
    #buscar.more_jobs()
    buscar.apply()

