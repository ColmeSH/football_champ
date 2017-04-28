from flask import Flask, render_template, request, redirect
from Classes.team import Team

app = Flask(__name__)
teams = []
# print teams

def search_team(teamid):
    for index, team in enumerate(teams):
        if teamid == index:
            return index


def generate_id(teams):
    try:
        return teams[-1].teamid + 1
    except:
        return 0


@app.route('/')
def index():
    return render_template('index.html', teams=teams)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # print 'sono in post'
        # create team with name passed by post method
        #check if string passed is empty and return a message or create a obj of class team
        if request.form['name'] != "":
            t = Team(request.form['name'])
            t.teamid = generate_id(teams)
            # print t.teamid

            teams.append(t)
            print teams
            return redirect('/')
        else:
            msg = "Please insert a football team name!"
            return render_template('createteam.html', msg=msg)

    else:
        print 'sono in get'
        return render_template('createteam.html')


@app.route('/details/team/<teamid>')
def details(teamid):
    teamid=int(teamid)
    i = search_team(teamid)
    i = int(i)
    print i
    return render_template('teamdetails.html', team=teams[i])

@app.route('')
def remove():
    pass



if __name__ == '__main__':
    app.run(debug=True)
