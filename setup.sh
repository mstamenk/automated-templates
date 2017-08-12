# BASH script to set up the working environment
# 
# Contains exclusively the locations of the folder
#
# Author: Marko Stamenkovic
# Site: https://mstamenk.github.io
# Mail: stamenkovim@gmail.com
#
# This is part of the Automated Templates tutorial
# Please visit :
# for more informations

export MYROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export DATABASE=$MYROOT/database
export ROUTINES=$MYROOT/routines
export TABLES=$MYROOT/tables
export TEMPLATES=$TABLES/templates

export PYTHONPATH=$PYTHONPATH:$DATABASE:$ROUTINES:$MYROOT:$TABLES:$TEMPLATES

alias clean='rm $TABLES/*.txt ; rm $TABLES/*.tex ; rm $TABLES/*.hpp '
alias db='python $ROUTINES/create_db.py'
