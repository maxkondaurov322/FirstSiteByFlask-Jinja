from flask import Flask, render_template
import json

from pip._internal.resolution.resolvelib import candidates

app = Flask(__name__)

def load_candidates_from_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    candidates = load_candidates_from_json('candidates.json')
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:candidate_id>')
def show_candidate(candidate_id):
    candidate = load_candidates_from_json('candidates.json')
    for candidate in candidate:
        if candidate['id'] == candidate_id:
            return render_template("candidate.html", candidate=candidate)
    return "Кандидат не найден", 404

@app.route("/search/<candidate_name>")
def search(candidate_name):
    candidates = load_candidates_from_json('candidates.json')
    matches = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            matches.append(candidate)
    count = len(matches)
    return render_template("search.html", candidates=matches, count=count)

@app.route("/skill/<skill_name>")
def skill(skill_name):
    candidates = load_candidates_from_json('candidates.json')
    matches = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower():
            matches.append(candidate)
    count = len(matches)
    return render_template("skill.html", candidates=matches, count=count, skill = skill_name)


if __name__ == '__main__':
    app.run(debug=True)
