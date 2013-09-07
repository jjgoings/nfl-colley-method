import getopt, sys
import numpy as np
from getdata import *
from colley import colley
from finalsort import *

def usage():
    print "usage: python %s [-e] -y <year>" % sys.argv[0]

def main():
    try:
        options, args = getopt.getopt(sys.argv[1:], "hy:e")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    year = None
    exhibition = False 
    for option,arg in options:
        if option   == '-y':
            year = int(arg)
        elif option == '-h':
            usage()
            sys.exit()
        elif option == '-e':
            exhibition = True 
    if year is None:
        usage();
        sys.exit(2)
   
    my_teamnames =  get_teams()
    my_games     =  get_games(year,exhibition)

    num_games = len(my_games)
    num_teams = len(my_teamnames)
    my_teams  = range(0,num_teams)
    ranking = colley(num_teams,num_games,my_teams,my_games,'none')
    write_sorted(my_teamnames,my_teams,ranking,'colley') 

if __name__ == "__main__":
    main()
