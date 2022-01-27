from email import message
from flask import render_template, request
from flask_login import login_user
import requests
from sqlalchemy import delete
from app import app
from forms import QueueForm
from models import User,Slider,QueueNumber
import json,xmltodict
import random
from datetime import date
import xml.etree.ElementTree as ET

@app.route("/home")
def home():
    slider_page = Slider.query.all()
    today=date.today()
    time = today.strftime("%d.%m.%Y")
    r = requests.get(f"https://www.cbar.az/currencies/{time}.xml")
    root = ET.fromstring(r.content)

    for i in root[1]:
        if i.attrib['Code'] == 'EUR':
            EUR = i[2].text

        if i.attrib['Code'] == 'GBP':
            GBP = i[2].text

        if i.attrib['Code'] == 'RUB':
            RUB = i[2].text

        if i.attrib['Code'] == 'USD':
            USD = i[2].text
        
        if i.attrib['Code'] == 'TRY':
            TRY = i[2].text
    return render_template('main.html',slider = slider_page,EUR=EUR,GBP=GBP,RUB=RUB,USD=USD,TRY=TRY)

    



@app.route("/queue", methods=['GET', 'POST'] )
def new():
    
    form = QueueForm()
    n = random.randint(1000000,9999999)

    if request.method =='POST':
        post_data = request.form
        form = QueueForm(data=post_data)
        if form.validate_on_submit():
            user = User(name=form.name.data,surname=form.surname.data,number=form.number.data,email=form.email.data,date=form.date.data,time=form.time.data)
            user.save()            
            
    elif request.method =='GET':

        number = QueueNumber(n)
        number.save()

    return render_template('new_queue.html',form = form,m=n)

@app.route("/online", methods=['GET', 'POST'])
def online():
    queue = QueueNumber.query.all()
    message = ''
    if request.method =='POST':
        number = request.form['queue']
        queue = QueueNumber.query.filter_by(queue=number).first()
        if queue:
            queue.delete()
        else:
            message = 'Növbə tapılmadı'
    return render_template('online_queue.html', message=message)



@app.route("/exchange", methods=['GET', 'POST'])
def exchange():
    todaytime = date.today().strftime("%d.%m.%Y")
    if request.method =='POST':
        selected_date = request.form['date']
        new_date = selected_date.split('-')
        todaytime = f"{new_date[2]}.{new_date[1]}.{new_date[0]}"
    response = requests.get(f'https://www.cbar.az/currencies/{todaytime}.xml', stream=True)
    data = xmltodict.parse(response.content)
    

    l_main = []

    for key, value in data.items():
        for a in value.items():
            if( isinstance(a[1], list) == True) :
                l_main.append(a[1])

    l_sub = l_main[0].copy()

    l_mini = l_sub[1].copy()

    l = l_mini.values()

    l_new = list(l)

    l_new_second = l_new[1]
  

    for i in l_new_second[0].items():
        dollar = (i[1])

    for i in l_new_second[20].items():
        chf = (i[1])
    
    for i in l_new_second[34].items():
        rub = (i[1])

    for i in l_new_second[1].items():
        euro = (i[1])

    for i in l_new_second[-29].items():
        sterling = (i[1])

    for i in l_new_second[28].items():
        tr = (i[1])

    for i in l_new_second[7].items():
        aed = (i[1])
    return render_template('exchange.html',value_aed = aed, value_tr = tr,value_chf = chf,value_rub = rub,value_pound = sterling, value_euro = euro , value_usd = dollar,day=todaytime)


