import json
from pathlib import Path

from app.services.chunking_service import chunk_text

DATA_PATH = Path(
    "app/data/agriculture_schemes.json"
)

def load_schemes():

    with open(
        DATA_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    documents = []

    for scheme in data:

        text = f"""
        Scheme Name:
        {scheme.get('name', '')}

        Category:
        {scheme.get('category', '')}

        Description:
        {scheme.get('description', '')}

        Benefits:
        {scheme.get('benefits', '')}

        Eligibility:
        {scheme.get('eligibility', '')}

        Required Documents:
        {', '.join(scheme.get('documents', []))}
        """

        # Create chunks
        chunks = chunk_text(text)

        # Store each chunk separately
        for chunk in chunks:

            documents.append({
                "scheme_name": scheme.get(
                    "name",
                    ""
                ),

                "text": chunk
            })

    return documents