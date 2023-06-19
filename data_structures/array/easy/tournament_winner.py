#https://www.algoexpert.io/questions/tournament-winner

# competitions: 
# [["home-team", "away-team"], []]
# 
# results:
# [0] -> home-team won
# [1] -> away-team won

HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    # initilize hashmap with a simple empty key so we can make comparisons
    best_team = ''
    scores = { best_team: 0 }

    for i in range(len(competitions)):        
        home_team, away_team = competitions[i]
        result = results[i]
        
        winning_team = home_team if result == HOME_TEAM_WON else away_team
        update_scores(winning_team, 3, scores)

        # update the best_team
        if scores[winning_team] > scores[best_team]:
                best_team = winning_team
    
    return best_team


def update_scores(winning_team, points, scores):
    if winning_team not in scores:
        scores[winning_team] = 0

    scores[winning_team] += points

# O(n) time -> where n is the number of competitions or results
# O(k) space -> for the keys that we are scoring. This problems limits the key length to 30 (30k + 1) Max 30 chars for each k
#               simplified to k (since 30 and 1 are constants)

# ------------------------------------------------------------------------------------

# This could be done to sort the array; O(n log(n)) -> NOT OPTIMAL
# sortedScores = sorted(scores.items(), key=lambda x: x[1])
# best_team = sortedScores[len(sortedScores)-1][0]


