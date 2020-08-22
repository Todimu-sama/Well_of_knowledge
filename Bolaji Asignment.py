'''
Bolaji's assignment
'''

'''
---------------------------------------------------------------------------------------------------
''' 
# question a

# checking if a team won, lost or drew the game
def has_won(team, result):
    if team == result[0]:
        if result[1] > result[3]:
            return True
        else:
            return False
    if team == result[2]:
        if result[3] > result[1]:
            return True
        else:
            return False
    return '{} has not yet played'.format(team)

def has_lost(team, result):
    if team == result[0]:
        if result[1] < result[3]:
            return True
        else:
            return False
    if team == result[2]:
        if result[3] < result[1]:
            return True
        else:
            return False
    return '{} has not yet played'.format(team)
        
def has_drawn(team, result):
    if team == result[0]:
        if result[1] == result[3]:
            return True
        else:
            return False
    if team == result[2]:
        if result[3] == result[1]:
            return True
        else:
            return False
    return '{} has not yet played'.format(team)

# get the number of goals scored for and against a team
def goals_for(team, result):
    if team == result[0]:
        return result[1]
    elif team == result[2]:
        return result[3]
    return '{} has not yet played'.format(team)
    
def goals_against(team, result):
    if team == result[0]:
        return result[3]
    elif team == result[2]:
        return result[1]
    return '{} has not yet played'.format(team)

'''
---------------------------------------------------------------------------------------------------
''' 
# question b
    
# statistics generation
def get_stats(results):
    stats = ['', 0, 0, 0, 0, 0, 0, 0, 0]
    for result in results:
        stats[0] = str(result[0])
        stats[1] = stats[1] + 1
        stats[5] = stats[5] + goals_for(result[0], result[1])
        stats[6] = stats[6] + goals_against(result[0], result[1])
        stats[7] = stats[7] + goals_for(result[0], result[1]) - goals_against(result[0], result[1])
        
        if has_won(result[0], result[1]) == True:
            stats[2] = stats[2] + 1
            stats[8] = stats[8] + 3
            
        elif has_drawn(result[0], result[1]) == True:
            stats[3] = stats[3] + 1
            stats[8] = stats[8] + 1
            
        elif  has_lost(result[0], result[1]) == True:
            stats[4] = stats[4] + 1
            
    statistics = (stats[0], stats[1], stats[2], stats[3],
                  stats[4], stats[5], stats[6], stats[7],
                  stats[8])
    
    return statistics

'''
---------------------------------------------------------------------------------------------------
''' 
# question c

def get_all_stats(results, teams):
    all_stats_list = []
    for team in teams:
        stat_list = []
        for result in results:
            if team == result[0]:
                stat_list.append(result)
        output = get_stats(stat_list)
        all_stats_list.append(output)
        
    return all_stats_list

'''
---------------------------------------------------------------------------------------------------
''' 
# question d

def show_table(statistics):
    print('---------------WORLD CUP TABLE GROUP STATISTICS---------------')
    print('%10s %3s %3s %3s %3s %3s %3s %4s %3s' % ('Team','P','W','D','L','F','A','GD','Pts'))
    statistics.sort(key=lambda x:x[8])
    
    for  i in range(len(statistics) - 1):
        statistic = statistics[i]
        print("%10s %3d %3d %3d %3d %3d %3d %4d %3d" % (statistic[0],statistic[1],
                 statistic[2],statistic[3],statistic[4],statistic[5],statistic[6],
                 statistic[7],statistic[8]))
        
'''
---------------------------------------------------------------------------------------------------
''' 

