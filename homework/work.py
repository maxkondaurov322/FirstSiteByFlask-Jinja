from flask import Flask
import json

app = Flask(__name__)
def load_candidates():
    with open('candidates.json', encoding='utf-8') as file:
        return json.load(file)


@app.route('/')
def main():
    result = "<pre>\n"
    for candidate in load_candidates():
        result += f"\nИмя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки через запятую - {candidate["skills"]}\n\n"
    result += "</pre>"
    return result

@app.route('/candidate/<int:candidate_id>')
def candidate_page(candidate_id):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return f"""
<img src="{candidate['picture']}">\n
<pre>
{candidate['name']} -
{candidate['position']}
{candidate['skills']}
</pre>
"""
    return "Кандидат не найден"


@app.route('/skills/<skills>')
def skills_page(skills):
    candidates = load_candidates()
    result = "<pre>\n"
    for candidate in candidates:
        candidate_skills = candidate['skills'].lower().split(", ")
        if skills in candidate["skills"]:
            result += f"\nИмя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки через запятую - {candidate["skills"]}\n\n"
    result += "</pre>"
    return result

app.run(debug=True)



