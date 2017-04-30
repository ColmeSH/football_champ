from flask import Flask, render_template, request, redirect
from Classes.team import Team, Tournament, TeamNotFound

app = Flask(__name__)
tournament = None


@app.route('/')
def index():
    return render_template('index.html', teams=tournament.teams)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        if request.form['name'] != "":
            team = Team(request.form['name'])
            tournament.add_team(team)
            return redirect('/')
        else:
            msg = "Please insert a football team name!"
            return render_template('createteam.html', msg=msg)

    else:
        return render_template('createteam.html')


@app.route('/details/team/<teamid>')
def details(teamid):
    try:
        teamid = int(teamid)
        index, team = tournament.get_team(teamid)
        print index, team
    except ValueError:
        return redirect('/')
    except TeamNotFound:
        return redirect('/')
    return render_template('teamdetails.html', team=team)


@app.route('/details/team/<teamid>/delete', methods=['POST'])
def delete(teamid):
    try:
        teamid=int(teamid)
        index, team = tournament.get_team(teamid)
    except ValueError:
        return redirect('/')
    except TeamNotFound:
        return redirect('/')
    tournament.teams.remove(tournament.teams[index])
    return redirect('/')


@app.route('/details/team/<teamid>/update', methods=['GET','POST'])
def update(teamid):
    try:
        teamid=int(teamid)
        index, team = tournament.get_team(teamid)
    except ValueError:
        return redirect('/')
    except TeamNotFound:
        return redirect('/')
    
    if request.method == 'POST':
        tournament.teams[index]['team'].name = request.form['name']
        return redirect('/')
    else:
        return render_template('update.html', team=team)


# @app.route('/api/teams')
# def api():
#     for i in tournament.teams:
#         print i.__dict__
#     return 'ciao'


if __name__ == '__main__':
    tournament = Tournament('AlexTest')
    app.run(debug=True)
