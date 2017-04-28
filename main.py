from flask import Flask, render_template, request, redirect
from Classes.team import Team

app = Flask(__name__)
teams = []
print teams

def search_team(teamid):
    for index, team in enumerate(teams):
        if teamid ==


def generate_id(teams):
    try:
        return teams[-1].teamid + 1
    except:
        return 1


@app.route('/')
def index():
    return render_template('index.html', teams=teams)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        print 'sono in post'
        # create team with name passed by post method
        if request.form['name'] != "":
            t = Team(request.form['name'])
            t.teamid = generate_id(teams)
            print t.teamid

            teams.append(t)
            print teams
            return redirect('/')
        else:
            msg = "Please insert a football team name!"
            return render_template('createteam.html', msg=msg)

    else:
        print 'sono in get'
        return render_template('createteam.html')


@app.route('/details/team/<teamid>', methods=['GET'])
def details(teamid):
    teamid=int(teamid)
    print search_team(teamid)
    return render_template('teamdetails.html', team=teams[teamid])



if __name__ == '__main__':
    app.run(debug=True)
