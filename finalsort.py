import numpy as np

def write_sorted(team_name,teams,rating,filename):
    #team_name = { 1 : 'B', 2 : 'D', 3 : 'E', 4 : 'A', 5 : 'C' }
    #print team_name
    
    #teams = np.array([ 1 , 2, 3, 4, 5])
    #print teams
    
    #rating = np.array([ 0.7, 0.5, 0.2, 0.9, 0.6])
    #print rating
    
    combine = np.vstack((rating,teams))
    
    sort_combine = np.array(sorted(combine.T,key=tuple,reverse=True))
    
    f = open(str(filename)+'.txt','w')
    for i in range(0,len(teams)):
       f.write(str(team_name[int(sort_combine[i,1])])+', '+str(sort_combine[i,0])+'\n')
    f.close()
