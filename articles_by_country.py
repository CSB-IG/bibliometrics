# coding: utf8
import argparse
from Bio import Medline
import time, datetime
import sys
from pprint import pprint

parser = argparse.ArgumentParser(description='grab adscriptions from medline')
parser.add_argument('medline', type=argparse.FileType('r'), default=sys.stdin)

args    = parser.parse_args()

from iso_3166 import countries

count = {}

adscriptions = set()
records = Medline.parse( args.medline )
for r in records:
    
    if 'AD' in r:
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

