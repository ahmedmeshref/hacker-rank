# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = list(reversed(sorted(set(scores))))
    for al_score in alice:
        while len(scores) > 0 and scores[-1] <= al_score:
            del scores[-1]
        print(len(scores) + 1)

scores = list(map(int, input().rstrip().split()))

alice = list(map(int, input().rstrip().split()))

result = climbingLeaderboard(scores, alice)

