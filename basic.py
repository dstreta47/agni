from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    drink= StringField("What would you like to have sir/madam?")
    submit= SubmitField("submit")

@app.route('/', methods= ['GET','POST'])
def index():
    drink= False 
    form= InfoForm()
    if form.validate_on_submit():
        drink= form.drink.data
        form.drink.data= ''
    return render_template('index.html', form = form, drink = drink) 


if __name__ == '__main__':
    app.run(debug=True)