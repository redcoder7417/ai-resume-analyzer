import spacy

nlp = spacy.load("en_core_web_sm")

# simple skill list (we will improve later)
SKILLS_DB = [
    "python", "java", "c++", "flask", "django",
    "react", "node", "mongodb", "sql", "machine learning",
    "deep learning", "nlp", "fastapi", "javascript"
]


def extract_skills(text):
    text_lower = text.lower()
    skills_found = []

    for skill in SKILLS_DB:
        if skill in text_lower:
            skills_found.append(skill)

    return list(set(skills_found))


def extract_entities(text):
    doc = nlp(text)

    entities = {
        "name": None,
        "organizations": [],
        "locations": []
    }

    for ent in doc.ents:
        if ent.label_ == "PERSON" and entities["name"] is None:
            entities["name"] = ent.text

        elif ent.label_ == "ORG":
            entities["organizations"].append(ent.text)

        elif ent.label_ == "GPE":
            entities["locations"].append(ent.text)

    return entities


def parse_resume(text):
    skills = extract_skills(text)
    entities = extract_entities(text)

    return {
        "name": entities["name"],
        "skills": skills,
        "organizations": entities["organizations"],
        "locations": entities["locations"]
    }