# Python script to fill the templates
#
# Author: Marko Stamenkovic
# Site: https://mstamenk.github.io
# Mail: stamenkovim@gmail.com
# 
# This is part of the Automated Templates tutorial
# Please visit: 
# for more informations

from routines.Analysis import loc, db ,dump, outfiles

# Example2 : C++ namespace
# Fill the namespace uniquely

outfiles.create('Analysis','Analysis','.hpp')
outfiles.fill_template('Analysis','example2.tmp',db)

# Example3 : Latex automated table
# Fill the latex table

outfiles.create('Latex','Latex','.tex')
outfiles.fill_template('Latex','example3.tmp',db)



