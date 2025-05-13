import json

def load_candidates_from_json(path):
    with open(path, encoding= 'utf-8') as f:
        return json.load(f)


def get_candidate(candidate_id):
    for candidate in load_candidates_from_json('candidates.json'):
        if candidate['id'] == candidate_id:
            return candidate

def get_candidate_by_name(candidate_name):
    for candidate in load_candidates_from_json('candidates.json'):
        if candidate['name'] == candidate_name:
            return candidate

def get_candidate_by_skill(candidate_skill):
    all_candidates = []
    for candidate in load_candidates_from_json('candidates.json'):
        skills = [skill.lower().strip() for skill in candidate['skills'].split(',')]
        if candidate_skill.lower() in skills:
            all_candidates.append(candidate)
    return all_candidates






