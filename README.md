# Bibliometrics




## articles_by_country.py and articles_by_year.py

Their input is a pubmed search saved in MEDLINE format.
The output is self-explanatory.

## mesh_network_from_medline.py

This script inputs a MEDLINE file, it will connect all meshterms found
in each record, if pairs are found more than once the weight of the
connection is increased.

It will output an edgelist thus formatted:

    source, target, weight

# How to run this software

The use of '''virtualenv''' is encouraged.

## Creating a virtual environment

    $ virtualenv /path/to/environments/bibliometrics
    $ source /path/to/environments/bibliometrics/bin/activate
    # active environments look like this
    (bibliometrics) $


## Install dependencies

    $ pip install -r requirements.txt


## Usage

Try running the scripts with -h for usage instructions. 
