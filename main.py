import csv
import re
import warnings


def bigg_models(downloads, artifacts):
    bigg_models_reactions = []

    with open(downloads / "bigg_models_reactions.txt") as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)
        for row in reader:
            if len(row) != 6:
                warnings.warn(f"Length must be 6 [{row}]")
                continue
            bigg_id, name, reaction_string, model_list, database_links, old_bigg_ids = row
            for xref in database_links.split(';'):
                xref = xref.strip()
                if xref == "":
                    continue
                mobj = re.match('^\s*([^:]+)\s*:\s*https?://identifiers.org/(\S+)', xref)
                assert mobj is not None, f"Failed to parse [{xref}]"
                db_name, db_id = mobj.group(1), mobj.group(2)
                bigg_models_reactions.append((f"bigg.reaction:{bigg_id}", db_id))

    bigg_models_metabolites = []

    with open(downloads / "bigg_models_metabolites.txt") as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)
        for row in reader:
            if len(row) != 6:
                warnings.warn(f"Length must be 6 [{row}]")
                continue
            bigg_id, universal_bigg_id, name, model_list, database_links, old_bigg_ids = row
            for xref in database_links.split(';'):
                xref = xref.strip()
                if xref == "":
                    continue
                mobj = re.match('^\s*([^:]+)\s*:\s*https?://identifiers.org/(\S+)', xref)
                assert mobj is not None, f"Failed to parse [{xref}]"
                db_name, db_id = mobj.group(1), mobj.group(2)
                bigg_models_metabolites.append((f"bigg.metabolite:{bigg_id}", db_id))

    with open(artifacts / "bigg_models.csv", "w") as f:
        writer = csv.writer(f)

        for row in bigg_models_reactions:
            writer.writerow(row)

        for row in bigg_models_metabolites:
            writer.writerow(row)


if __name__ == "__main__":
    from pathlib import Path

    downloads, artifacts = Path('downloads'), Path('artifacts')

    with open(artifacts / "output1.txt", "w") as f:
        f.write("Saluton, Mondo!\n")

    bigg_models(downloads, artifacts)
