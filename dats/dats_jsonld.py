from pyld import jsonld
import json
import os


doc = json.load(open(os.join(".." + os.sep  + "json-instances" + os.sep  + "", "PDB-5AEM.jsonld")))

print("loaded jsonld", doc)

context = json.load(open(os.join(".." + os.sep  + "json-schemas" + os.sep  + "contexts" + os.sep, "dataset_sdo_context.jsonld")))

print("loaded context")

compacted = jsonld.compact(doc, context)

print("-------------COMPACTED")

print(json.dumps(compacted, indent=2))

expanded = jsonld.expand(compacted)

print("-------------EXPANDED")

print(json.dumps(expanded, indent=2))

flattened = jsonld.flatten(compacted)
