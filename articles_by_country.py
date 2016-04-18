# coding: utf8
import argparse
from Bio import Medline
import time, datetime
from pprint import pprint

parser = argparse.ArgumentParser(description='grab adscriptions from medline')
parser.add_argument('--citations', type=argparse.FileType('r'), required=True)

args    = parser.parse_args()


from iso_3166 import countries

count = {}

adscriptions = set()
records = Medline.parse( args.citations )
for r in records:
    
    # evenly format dates
    if 'CRDT' in r.keys():
        conv = time.strptime( r['CRDT'][0], "%Y/%m/%d %H:%M" )
        r['CRDT'] = datetime.datetime(*conv[:6]) # date created
    if 'DCOM' in r.keys():
        conv = time.strptime( r['DCOM'], "%Y%m%d" )
        r['DCOM'] = datetime.datetime(*conv[:6]) # date completed
    if 'LR' in r.keys():
        conv = time.strptime( r['LR'], "%Y%m%d" )
        r['LR'] = datetime.datetime(*conv[:6]) # date revised
    if 'DEP' in r.keys():
        conv = time.strptime( r['DEP'], "%Y%m%d" )
        r['DEP'] = datetime.datetime(*conv[:6]) # date of electronic publication

    # let PubMed handle keys
    r['_id'] = int(r['PMID'])

    if 'AD' in r:
#        print r['PMID']
#        pprint(r['AD'])
        ad = [n.replace('.','').replace(',','').replace(':','').replace(';','') for n in r['AD'].split()]
        for country in countries:
            c = country
            if c in ad:

                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1


for c in count:
    print "%s,%s" % (c, count[c])

