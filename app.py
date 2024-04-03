from flask import Flask, render_template, request, make_response, redirect, url_for, session, abort

app = Flask(__name__)
app.secret_key = 'ada4tgferg455rh654we3aaeawe'



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    print(session)
    return render_template('about.html')

@app.route('/contact')
def contact():
    contacts=[{"name":'Nikita', 'number': '56(80)215-41-30'},
          {"name":'Kostya', 'number': '52(4830)907-93-58'},
          {"name":'Sultan', 'number': '1(923)761-30-36'},
          {"name":'Nurbakhyt', 'number': '9(38)126-71-64'},
          {"name":'Altair', 'number': '0(03)424-83-24'},
          {"name":'Artem', 'number': '54(2583)699-85-70'},
          {"name":'Slava', 'number': '2(32)646-88-41'},
          {"name":'Sancho', 'number': '8(6359)426-02-69'},
          {"name":'Alisher', 'number': '391(047)029-90-41'},
          {"name":'Diego', 'number': '2(8537)700-83-67'},]
    return render_template('contact.html', contacts=contacts)


if __name__ == '__main__':
    app.run(debug=True)