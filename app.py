from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route("/")
def all_candidates():
    """Главная страница"""
    candidates = utils.get_all()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:pk>")
def candidates_pk(pk):
    """Стрница кандидатов по pk"""
    candidate = utils.get_by_pk(pk)
    name = candidate['name']
    position = candidate['position']
    picture = candidate['picture']
    skills = candidate['skills']
    return render_template('card.html', name=name, position=position, picture=picture, skills=skills)


@app.route("/search/<candidate_name>")
def candidates_name(candidate_name):
    """Стрница кандидатов по name"""
    list_candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', list_candidates=list_candidates, len_candidates=len(list_candidates))


@app.route("/skill/<skill_name>")
def candidates_skill(skill_name):
    """Стрница кандидатов по skill"""
    list_candidates = utils.get_by_skill(skill_name)
    # skill = skill_name
    return render_template('skill.html', list_candidates=list_candidates, len_candidates=len(list_candidates),
                           skill_name=skill_name)


app.run()
