from test_framework import generic_test


from collections import defaultdict
def num_combinations_for_final_score(final_score, individual_play_scores):
    print(final_score, individual_play_scores)
    # TODO - you fill in here.

    scoreWays = [[0 for i in range(final_score+1)] for j in range(len(individual_play_scores))]
    for i in range(len(individual_play_scores)):
        scoreWays[i][0] = 1

    for i,indvidualScore in enumerate(individual_play_scores):
        if i == 0:
            for score in range(indvidualScore,final_score+1):
                scoreWays[i][score] = scoreWays[i][score - indvidualScore]
        else:
            for score in range(1,final_score+1):
                if score >= indvidualScore:
                    scoreWays[i][score] = scoreWays[i][score-indvidualScore] + scoreWays[i-1][score]
                else:
                    scoreWays[i][score] = scoreWays[i - 1][score]

    return scoreWays[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
