from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

columns = ['name', 'age', 'gender', 'budget', 'area', 'roommates_needed', 'cleanliness', 'bedtime', 'friends_over', 'friend_level', 'pets', 'loud', 'most_important']
df_users = pd.DataFrame(columns=columns)
global df_users

# this is the main route -- aka, it displays the form initially
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/match")
def parse_form():
    if request.method == "POST":
        form_data = {field: request.form.get(field) for field in columns}
        df_users.loc[len(df)] = form_data
    





