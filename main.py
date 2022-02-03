import csv


def bigg_models(downloads, artifacts):
    bigg_models_reactions = []
    with open(downloads / "bigg_models_reactions.txt") as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)
        for row in reader:
            bigg_id, name, reaction_string, model_list, database_links, old_bigg_ids = row
            for xref in database_links.split(';'):
                db_name, db_id = xref.split(':')
                db_name, db_id = db_name.strip(), db_id.strip()
                assert db_id.startswith('http://identifiers.org')
                bigg_models_reactions.append((f"https://identifiers.org/bigg.reaction:{bigg_id}", db_id))
    
    with open(artifacts / "bigg_models_reactions.csv", "w") as f:
        writer = csv.writer(f)
        for row in bigg_models_reactions:
            writer.writerow(row)


if __name__ == "__main__":
    from pathlib import Path
    
    downloads, artifacts = Path('downloads'), Path('artifacts')
    
    with open(artifacts / "output1.txt", "w") as f:
        f.write("Saluton, Mondo!\n")

    bigg_models(downloads, artifacts)
