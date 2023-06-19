# ****************************************************************
# Name: Wing Lok LO
# Link: https://replit.com/join/wdcvgxffld-lowinglokjason
# ****************************************************************

from flask import Flask,render_template
app = Flask('app')

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/lic')
def licenses():
  return render_template("lic.html")

@app.route('/exp')
def experience():
  return render_template("exp.html")
  
@app.route('/edu')
def education():
  return render_template("edu.html")

@app.route('/skill')
def skills():
  return render_template("skill.html")

@app.route('/weather')
def weather():
  return render_template('weather.html')

@app.route('/bmi')
def bmi():
  return render_template('bmi.html')

app.run(host='0.0.0.0', port=8080)