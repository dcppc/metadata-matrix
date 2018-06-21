# Metadata_matrix
### Extraction of MonDO-DO and Uberon-FMA mappings from MONDO and uberon owl files and generating JSON files.
_**1. Extracting MonDO - DO and Uberon - FMA mappings**_

Many MonDO (Monarch Disease Ontology) classes have database_cross_reference annotations to Disease Ontology (DO) classes in the mondo.owl file. Similarly, Uberon classes have database_cross_reference annotations to FMA classes in uberon.owl file. These cross references represent instances in which the classes have the same semantic meaning. SPARQL queries can extract the DOID or FMA cross reference annotations and provide a spreadsheet output with the labels of each mapped class. This is done by merging DO with MonDO (or Uberon with FMA), finding the database_cross_reference IDs, and then finding the DO (or FMA) class that matches that ID. These queries can be run through any triple store, but we recommend installing ROBOT to easily merge and then query the ontologies.

* The ROBOT installation guidelines are available here: http://robot.obolibrary.org/

* Save the following SPARQL query as **mondo-do.rq**. This query will be executed by ROBOT (using the command specified shortly) to find the cross reference IDs, the MonDO class ID that the cross reference is on, and the label for the DO class referenced. The output is in CSV format, though you can change it to TSV if you prefer.

```
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?id ?label ?doid ?dolabel WHERE {
    ?s oboInOwl:hasDbXref ?ref .
    ?s rdfs:label ?label .
    OPTIONAL { ?s oboInOwl:id ?id }
    FILTER regex(?ref, "DOID:[0-9]{1,7}")
    ?do oboInOwl:id ?doid .
    FILTER (str(?ref) = str(?doid))
    ?do rdfs:label ?dolabel .
}
```

* To extract the Uberon-FMA mappings, save this query as **uberon-fma.rq**.
```
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?id ?label ?fmaid ?fmalabel WHERE {
    ?s oboInOwl:hasDbXref ?ref .
    ?s rdfs:label ?label .
    OPTIONAL { ?s oboInOwl:id ?id }
    FILTER regex(?ref, "FMA:[0-9]{1,7}")
    ?fma oboInOwl:id ?fmaid .
    FILTER (str(?ref) = str(?fmaid))
    ?fma rdfs:label ?fmalabel .
}
```
* After saving the SPARQL queries, run the following ROBOT command at the terminal in the directory that you saved the queries to. This first command will first merge MonDO and DO, and then execute the SPARQL query on the merged ontology to generate the mappings. Be aware that this query could take some time, as both MonDO and DO are very large ontologies and need to be downloaded from the input IRIs.
```
robot merge --input-iri http://purl.obolibrary.org/obo/mondo.owl --input-iri http://purl.obolibrary.org/obo/doid.owl query --format csv --query mondo-do.rq mondo_doid.csv
```
A pre-generated MonDO-DO mapping file can be found here:
https://github.com/dcppc-phosphorous/Metadata_matrix/blob/master/mondo_doid.csv

* The following ROBOT command will merge Uberon and FMA owl files to execute the SPARQL query to output the mappings into a csv (comma separated values) file.
```
robot merge --input-iri http://purl.obolibrary.org/obo/uberon.owl --input-iri http://purl.obolibrary.org/obo/fma.owl query --format csv --query uberon-fma.rq uberon_fma.csv
```

The uberon-fma.csv can be found here:
https://github.com/dcppc-phosphorous/Metadata_matrix/blob/master/uberon_fma.csv 

_**2. Generating JSON mapping files**_

The CSV files generated from STEP 1 are used as input to generate JSON mapping files.

The python code for generating mondo-do json mapping file using mondo_doid.csv is here,
https://github.com/dcppc-phosphorous/Metadata_matrix/blob/master/make_mapping_mondo_do.py

The python code for generating uberon-fma json mapping file using uberon_fma.csv is here,
https://github.com/dcppc-phosphorous/Metadata_matrix/blob/master/make_mapping_uberon_fma.py

The mondo-do json mapping file is here,
https://github.com/dcppc-phosphorous/Metadata_matrix/blob/master/mondo_do_mapping.json

The uberon-fma json mapping file is here,
https://github.com/dcppc-phosphorous/Metadata_matrix/blob/master/uberon_fma_mapping.json





