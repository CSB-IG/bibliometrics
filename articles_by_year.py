import argparse
from Bio import Medline
import time, datetime
import sys
from pprint import pprint

parser = argparse.ArgumentParser(description='Prints to stdout a table of number of publications per year for medline input.')
parser.add_argument('medline', type=argparse.FileType('r'), default=sys.stdin, help="citations file in medline format")
args    = parser.parse_args()

count = {}

records = Medline.parse( args.medline )
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
    if 'DA' in r.keys():
        conv = time.strptime( r['DA'], "%Y%m%d" )
        r['DA'] = datetime.datetime(*conv[:6]) # date revised

        

    if 'CRDT' in r:
        year = r['CRDT'].year
    elif 'DCOM' in r:
        year = r.get('DCOM').year
    elif 'DA' in r:
        year = r.get('DA').year
    else:
        exit(1) # no usable date found
        #pprint(r)

    if year in count:
        count[year] += 1
    else:
        count[year] = 1



for c in count:
    print "%s,%s" % (c, count[c])

