!pip install bioservices
!pip install pandas
!pip install pyensemblrest
from bioservices import *
import json
import re
import numpy as np
import pandas as pd
from ensemblrest import EnsemblRest


xi = HGNC()
ensRest = EnsemblRest()


ii = xi.fetch('hgnc_id', '620')
iii = ii['response']
iv = iii['docs']
v = iv[0]

if type(v) is dict:
  print("dict")
  
kv = v['symbol'], v['name'], v['location']
inf = v['entrez_id'], v['pubmed_id'], v['refseq_accession'], v['ensembl_gene_id']

print(kv)
print(inf)


ens_gene_id = v['ensembl_gene_id']

print(ens_gene_id)


gsr = ensRest.getSequenceById(id=ens_gene_id)
#print(gsr)

print("LOCATION:  " + gsr['desc'])
print(gsr['seq'])
