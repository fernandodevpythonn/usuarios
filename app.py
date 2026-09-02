from controllers.basico_controller import basico_controller
from database.connection import BancoMysql
from database.tables import BancoTabelas
from dotenv import load_dotenv
import os
from flask import Flask
banco = BancoMysql()
tabelas = BancoTabelas(banco)
tabelas.criar_tabelas()
load_dotenv()

app = Flask(__name__)
basico_controller(app)

if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG","False").lower()=="true")