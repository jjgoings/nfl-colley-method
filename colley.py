import numpy as np

def colley(num_teams,num_games,my_teams,my_games,weighting):
    winmargin = 0.0
    m = num_games
    A = np.zeros((num_teams,num_teams))
    wins = np.zeros(num_teams)
    losses = np.zeros(num_teams)
    total = np.zeros(num_teams)
  
    if weighting == 'none':
      def g(t):
        return 1.0
    elif weighting == 'linear':
      def g(t):
        t0 = my_games[0,0]
        tf = my_games[m-1,0]
        return (t - t0)/(tf - t0)
    elif weighting == 'log':
      def g(t):
        t0 = my_games[0,0]
        tf = my_games[m-1,0]
        return np.log(1 + (t/tf))
    elif weighting == 'exponential':
      def g(t):
        t0 = my_games[0,0]
        tf = my_games[m-1,0]
        return np.exp((t-t0)/(tf-t0))
    elif weighting == 'biweekly':
      def g(t):
        t0 = my_games[0,0]
        tf = my_games[m-1,0]
        return math.floor(((t-t0)/14)+1)
  
    for game in range(0,m):
      #if (my_games[game,3] == 1):
      #  my_games[game,4] = my_games[game,4] - homeadvantage
      #elif (my_games[game,6] == 1):
      #  my_games[game,7] = my_games[game,7] - homeadvantage
      #else:
      #  continue
      w = my_games[game,2] - 1.0
      l = my_games[game,5] - 1.0
      #if (my_games[game,4] == my_games[game,7]): # don't count ties
      #  continue
      if abs(my_games[game,4] - my_games[game,7]) <= winmargin:
        A[w,w] = A[w,w] + 1.0*g(my_games[game,0])
        A[l,l] = A[l,l] + 1.0*g(my_games[game,0])
        A[l,w] = A[l,w] - 1.0*g(my_games[game,0])
        A[w,l] = A[w,l] - 1.0*g(my_games[game,0])
      else:
        A[l,w] = A[l,w] - 1.0*g(my_games[game,0])
        A[w,l] = A[w,l] - 1.0*g(my_games[game,0])
        wins[w] = wins[w] + 1.0*g(my_games[game,0])
        losses[l] = losses[l] + 1.0*g(my_games[game,0])
  
    for i in range(0,num_teams):
      total[i] = total[i] + wins[i] + losses[i]
  
    b = np.zeros(num_teams)
    for i in range(0,num_teams):
      A[i,i] = 2 + total[i] + A[i,i]
      b[i] = 1 + (wins[i] - losses[i])/2
    
    
    x = np.linalg.solve(A,b)
    #np.savetxt('colley_raw.csv',x,delimiter=",")
    return x 

