from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "HALLO KAMI DARI KELOMPOK 5 YANG BERANGGOTAKAN 6 ORANG"
