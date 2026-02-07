from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import logging as lg


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

class Etudiants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(100),nullable=False)
    nom = db.Column(db.String(50), nullable = False)
    classe = db.Column(db.String(100), nullable = False)
    

    def __init__(self,prenom,nom,classe):
        self.prenom = prenom
        self.nom = nom
        self.classe = classe

with app.app_context(): db.create_all()


# def init_db():
#     db.drop_all()
#     db.create_all()
#     db.session.add(Etudiants("John", "Doe", "1A"))
#     db.session.add(Etudiants("Jane", "Doe", "1B"))
#     db.session.commit()
#     lg.warning('Database initialized!')

@app.route('/')
@app.route('/connexion', methods=["post"])
@app.route('/connexion/')
def connexion():
    prenom = request.form.get('username')
    nom = request.form.get('password')
    
    etu = Etudiants.query.filter_by(prenom=prenom,nom=nom).first()
    if etu:
        EtudiantAll =  Etudiants.query.all()
        return render_template('index.html',EtudiantAll=EtudiantAll)

    return render_template('connexion.html')

@app.route('/index')
@app.route('/index/')
def Hello():
    EtudiantAll =  Etudiants.query.all()
    return render_template('index.html', EtudiantAll=EtudiantAll)

@app.route('/add', methods=["post"])
@app.route('/add/')
def add():
    prenom = request.form.get('prenom')
    nom = request.form.get('nom')
    classe = request.form.get('classe')
    
    if prenom and nom and classe:
        db.session.add(Etudiants(prenom=prenom,nom=nom,classe=classe))
        db.session.commit()
    return render_template('addEtudiant.html')



