import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

#pour générer les clés secret on aura besoin les 2 lignes
#import random,string
#"".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY= 'zy#}v/1<!UpV=Ti "XD1P / ' #permet de générer toutes les données chiffrées
