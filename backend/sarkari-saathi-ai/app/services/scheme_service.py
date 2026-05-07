import json

def load_schemes():
    with open("app/data/schemes.json", "r", encoding="utf-8") as f:
        return json.load(f)


def search_schemes(query: str):
    schemes = load_schemes()
    results = []

    for scheme in schemes:
        if query.lower() in scheme["name"].lower() or \
           query.lower() in scheme["eligibility"].lower() or \
           query.lower() in scheme["category"].lower():
            results.append(scheme)

    return results