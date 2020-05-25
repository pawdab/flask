from flask import Flask

app = Flask(__name__)

from flask import request, redirect

from flask import render_template

@app.route('/me', methods=['GET'])
def meme():
       return render_template("me.html")

# jak rozumiem chodziło o printy, które poniżej wykomentowałem?
@app.route('/contact', methods=['GET', 'POST'])
def contactz():
   if request.method == 'GET':
       #print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       #print("We received POST")
       #x = str(request.form['element'])
       #print("z formularza:" + x)
       return redirect("/contact")


