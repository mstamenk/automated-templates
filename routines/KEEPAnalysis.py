# Python script to handle the relative informations to the Analysis + Utility functions
# 
# Authors: Luca Pescatore, Marko Stamenkovic
# Site: http://pluca.webnode.com/ , https://mstamenk.github.io
# Mails: luca.pescatore@cern.ch , stamenkovim@gmail.com
#
# This file is part of the Automated Templates tutorial
# Please visit:
# for more informations.

import os
import string

# Fetch the locations

class loc : pass

loc.MYROOT = os.getenv('MYROOT') + '/'
loc.DATABASE = os.getenv('DATABASE') + '/'
loc.ROUTINES = os.getenv('ROUTINES') + '/'
loc.TABLES = os.getenv('TABLES') + '/'
loc.TEMPLATES = os.getenv('TEMPLATES') + '/'

class Outfiles:
    def __init__(self):
        
        if not os.path.exists(loc.DATABASE+'outfiles_list.txt') :
            f = open(loc.DATABASE+'outfiles_list.txt','w')
            f.close()
        lines = open(loc.DATABASE+'outfiles_list.txt').readlines()
        self.files = {}
        for l in lines :
            toks = l.split()
            self.files[toks[0]] = toks[1]

    def writeline(self,name,text,clear=False):
        self.write(name,text+"\n",clear)

    def write(self,name,text,clear=False):
        if clear : f = open(self.files[name],'w')
        else : f = open(self.files[name],"a")
        f.write(text)
        f.close()
    def fill_template(self,name,template,dic) :
        tmp = open(loc.TEMPLATES+template)
        out = tmp.read().format(**dic)

        self.write(name,out,clear=True)
    
    def create(self,name,filename=None,extension=".txt"):
        if filename == None: filename = name
        if "." not in filename : filename += extension

        path = loc.TABLES + filename
        self.files[name] = path

        f = open(loc.DATABASE+'outfiles_list.txt','w')
        for n,p in self.files.iteritems() :
            f.write(n+" "+p)

outfiles = Outfiles()

import pickle

db = pickle.load(open(loc.DATABASE+'db.pkl'))

def dump(dataB,name):
    pickle.dump(dataB,open(loc.DATABASE+name,'w'))

# Automatically added by routines/create_db.py


        
def dumpAll():
    dump(db,'db.pkl')
    # Automatically added in dumpAll() by routines/create_db.py

