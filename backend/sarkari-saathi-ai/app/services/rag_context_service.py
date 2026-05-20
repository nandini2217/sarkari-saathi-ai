def build_context(results):
    context = ""

    for idx, scheme in enumerate(results, start=1):
        context += f"""
Scheme {idx}

Name:
{scheme.get("name", "")}

Category:
{scheme.get("category", "")}

Eligibility:
{scheme.get("eligibility", "")}

Benefits:
{scheme.get("benefits", "")}

Description:
{scheme.get("description", "")}

Documents:
{", ".join(scheme.get("documents", []))}

-----------------------------------
"""

    return context