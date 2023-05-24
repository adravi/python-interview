#https://www.algoexpert.io/questions/tournament-winner

# competitions: 
# [["home-team", "away-team"], []]
# 
# results:
# [0] -> home-team won
# [1] -> away-team won

HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    # Initilize hashmap with a simple empty key so we can make comparisons
    bestTeam = ''
    scores = { bestTeam: 0 }

    for i in range(len(competitions)):        
        homeTeam, awayTeam = competitions[i]
        result = results[i]
        
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
        updateScores(winningTeam, 3, scores)

        # Update the bestTeam
        if scores[winningTeam] > scores[bestTeam]:
                bestTeam = winningTeam
    
    return bestTeam


def updateScores(winningTeam, points, scores):
    if winningTeam not in scores:
        scores[winningTeam] = 0

    scores[winningTeam] += points

# O(n) T -> where n is the number of competitions or results
# O(k) S -> for the keys that we are scoring. This problems limits the key length to 30 (30k + 1) Max 30 chars for each k
#           simplified to k (since 30 and 1 are constants)

# ------------------------------------------------------------------------------------

# This could be done to sort the array; O(n log(n)) -> NOT OPTIMAL
# sortedScores = sorted(scores.items(), key=lambda x: x[1])
# bestTeam = sortedScores[len(sortedScores)-1][0]


