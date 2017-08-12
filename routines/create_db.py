# Python script to create empty .pkl databases and load them in routines/Analysis.py
#
# Author: Marko Stamenkovic
# Site: https://mstamenk.github.io
# Mail: stamenkovim@gmail.com
#
# This is part of the Automated Templates tutorial
# Please visit: 
# for more informations.

import sys
from routines.Analysis import loc


def extension(filename):
    if '.pkl' in filename:
        output = filename
    else: 
        output = filename+'.pkl'
        print("The extension .pkl was added to the file name!")
    return output

def split(filename):
    l = filename.split('.')
    name = l[0]
    ext = '.' + l[1]
    return name, ext

# Create the .pkl file in $DATABASE

filename = extension(sys.argv[1])
init = '(dp0\n.'

f = open(loc.DATABASE+filename,'w')
f.write(init)
f.close()

# Load it in routines/Analysis.py

flag = '# Automatically added by routines/create_db.py'
flag2 = '    # Automatically added in dumpAll() by routines/create_db.py'


name, ext = split(filename)
add = "\n{name} = pickle.load(open(loc.DATABASE+'{filename}'))".format(name=name, filename=filename)
add2 = '\n    dump({name},"{filename}")'.format(name=name,filename=filename)

# Read file + add the lines
r = open(loc.ROUTINES+'Analysis.py','r')
out = r.read()

if flag in out and flag2 in out:
    out = out.replace(flag,flag+add)
    out = out.replace(flag2,flag2+add2)
else: print('Please defines flag and flag2 variables in order to add new lines to routines/Analysis.py')
r.close()

# Create a new file routines/Analysis.py and write the new commands in
with open(loc.ROUTINES+'Analysis.py','w') as r:
    r.write(out)
    r.truncate()
    r.close()


