from flask import Flask, render_template, request
from Classes.team import Team
app = Flask(__name__)
teams = []
print teams


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'POST':
        print 'sono in post'
        #create team with name passed by post method
        t = Team(request.form['team'])
        teams.append(t)

        return request.form['team']
    else:
        print 'sono in get'
        return render_template('createteam.html')













if __name__=='__main__':
    app.run(debug=True)