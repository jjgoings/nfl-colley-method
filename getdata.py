import sys
import urllib
from numpy import genfromtxt
import numpy as np

def get_teams():
    f = urllib.urlopen("http://www.masseyratings.com/scores.php?s=199229&sub=199229&all=1&mode=3&exhib=on&format=2")
    s = f.read().split()
    my_teamnames = {} 
    for i in range(0,len(s)/2):
        my_teamnames.update({i : s[i*2 + 1]})
    return my_teamnames

def get_games(year,exhibition):
    if year == 2013:
        if exhibition == True:
            f = urllib.urlopen('http://www.masseyratings.com/scores.php?s=199229&sub=199229&all=1&mode=3&exhib=on&format=1')
        elif exhibition == False:
            f = urllib.urlopen('http://www.masseyratings.com/scores.php?s=199229&sub=199229&all=1&mode=3&format=1')
        else:
            sys.exit('"exhibition" must be "True" or "False"')
    elif year == 2012:
        if exhibition == True:
            f = urllib.urlopen('http://www.masseyratings.com/scores.php?s=181613&sub=181613&all=1&mode=3&exhib=on&format=1')
        elif exhibition == False:
            f = urllib.urlopen('http://www.masseyratings.com/scores.php?s=181613&sub=181613&all=1&mode=3&format=1')
        else:
            sys.exit('"exhibition" must be "True" or "False"')
    else:
        sys.exit('Not a valid year')
    s = f.read()
    if exhibition == False:
        file_name = str('games_'+str(year)+'.txt')
    elif exhibition == True:
        file_name = str('games_'+str(year)+'_exhib.txt')
    k = open(file_name,'w')
    k.write(s)
    k.close()
    f.close()

    my_games = genfromtxt(file_name, dtype = None, delimiter=',')
   
    return my_games


