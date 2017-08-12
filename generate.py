# Python script to generate the database
#
# Author: Marko Stamenkovic
# Site: https://mstamenk.github.io
# Mail: stamenkovim@gmail.com
# 
# This is part of the Automated Templates tutorial
# Please visit: 
# for more informations.

from routines.Analysis import loc, db, dump, outfiles 

# Example 1 : Fill 2 text files with one template.
# Template requirement: {USER[NAME]} and {USER[SITE]}

users = { 'Luca'  : 'http://pluca.webnode.com/',
          'Marko' : 'https://mstamenk.github.io',
          # Fill here for your personal informations
        }

db['USER'] =  { 'NAME' : 'Luca', 
                'SITE' : users['Luca']}

outfiles.create('Luca','Luca','.txt')
outfiles.fill_template('Luca','example1.tmp',db)

db['USER'] =  { 'NAME' : 'Marko',
                'SITE' : users['Marko']}


outfiles.create('Marko','Marko','.txt')
outfiles.fill_template('Marko','example1.tmp',db)

# Example2 : C++ namespace 
# In this script, only fill the db dictionary and save it to use later

db['GRAVITY'] = 9.81  # [m s^-2]
db['MASS'] = 80       # [kg]
db['HEIGHT'] = 20     # [m]

db['POTENTIAL'] = db['MASS'] * db['GRAVITY'] * db['HEIGHT'] # Epot = m*g*h

dump(db,'db.pkl')

# Example3 : Latex automated table
# Solve y=f(x)=a ^ x for first, second and third order

a = 127

db['first']  = a**1
db['second'] = a**2
db['third']  = a**3

db['a'] = a

dump(db,'db.pkl') 






