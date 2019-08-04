!pip install biopython
!pip install pandas
!pip install biopandas

import numpy as np
import pandas as pd
from biopandas import pdb
from biopandas.pdb import PandasPdb

from Bio.PDB.PDBParser import PDBParser
parser = PDBParser(PERMISSIVE=1)

from Bio.PDB.MMCIFParser import MMCIFParser
parser = MMCIFParser()

from Bio.PDB.MMCIF2Dict import MMCIF2Dict


#google colab upload from local

from google.colab import files
uploaded = files.upload()

f = open("3eiy.cif")

structure_id = "3eiy"
filename = "3eiy.cif"
structure = parser.get_structure(structure_id, filename)

#local upload section end

#fetch

ppdb = PandasPdb().fetch_pdb('3eiy')

#fetch end


x = ppdb.df['ATOM'].head(100)
x.set_index("residue_number", inplace=True)
grouped = x.groupby(level=0)



#INITIALIZE LISTS
group_list = []
xList = []
yList = []
zList = []
residue_list = []


#FILL GROUP_LIST
for name, group in grouped:
  group_list.append(name)
  
  
  
  
  
#FILL XLIST, YLIST, ZLIST, RESIDUE_LIST

for i in group_list:
  res_groups = grouped.get_group(i)
  groupby_res_name = res_groups.groupby("residue_name").first().reset_index()
  res_names = groupby_res_name.iat[0,0]
  residue_list.append(res_names)
  
  xCo = res_groups[['x_coord']]
  xCoMean = xCo.mean()
  xList.append(xCoMean)
  
  yCo = res_groups[['y_coord']]
  yCoMean = yCo.mean()
  yList.append(yCoMean)
  
  zCo = res_groups[['z_coord']]
  zCoMean = zCo.mean()
  zList.append(zCoMean)
  continue
  
  
  
  
#LISTS TO 1D ARRAYS 
  
xRay = np.asarray(xList)
yRay = np.asarray(yList)
zRay = np.asarray(zList)
resRay = np.asarray(residue_list)


#FLIP AXIS/LAYOUT
rRay = np.vstack(resRay)

#CONCATENATE THE ARRAYS
rxyzRay = np.concatenate((rRay, xRay, yRay, zRay), 1)


#FORMAT AS DATAFRAME WITH COLUMN NAMES
df = pd.DataFrame(rxyzRay, columns=['Residue', 'X', 'Y', 'Z'])






