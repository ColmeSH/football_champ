from flask import Flask, render_template, request, redirect
from Classes.team import Team
from random import randint

app = Flask(__name__)
teams = []
# print teams

def search_team(teamid):
    teamid = int(teamid)
    for index, team in enumerate(teams):
        if team.teamid == teamid:
            return index


def generate_id():
    try:
        return teams[-1].teamid + 1
    except IndexError:
        return 1


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
            t.points = randint(1,100)
            t.teamid = generate_id()
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
    index = search_team(teamid)
    print index
    return render_template('teamdetails.html', team=teams[index])

@app.route('/details/team/<teamid>/delete', methods=['POST'])
def delete(teamid):
    # print teamid
    teamid = int(teamid)
    index = search_team(teamid)
    # print 'wanna delete football team "{}"'.format(teams[index].name)
    # print type(teamid), type(index)
    if teams[index].teamid == teamid:
        teams.remove(teams[index])
        print 'rimosso ATTENZIONE ALLA RICERCA DEL BLOG!!!!!!!!!!!!!!!!!!!!'
        return redirect('/')
    return 'non sto rimuovendo'

@app.route('/details/team/<teamid>/update', methods=['GET','POST'])
def update(teamid):
    teamid=int(teamid)
    index=search_team(teamid)

    if request.method == 'POST':
        print 'sono in post di update'
        print teams[index].name
        print request.form['name']
        teams[index].name = request.form['name']
        print teams[index].name
        return render_template('index.html', teams=teams)
    else:
        print 'sono in get di update'
        return render_template('update.html', team=teams[index])





if __name__ == '__main__':
    app.run(debug=True)