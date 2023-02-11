# -*- coding: utf-8 -*-
class Solution(object):
    # Runtime 1461 ms / Memory 13.8 MB
    def bestTeamScore_1(self, scores, ages):
        people = []
        for idx, age in enumerate(ages):
            people.append((age, scores[idx]))
        people.sort(key = lambda s: (s[0], s[1]) ) #多重排序
        
        dp = [0] * len(people)
        for i in range(len(dp)):
            dp[i] = people[i][1]
            for j in range(i):
                if people[i][1] >= people[j][1]:
                    dp[i] = max(dp[i], dp[j]+people[i][1])
        return max(dp)

    # Runtime 387 ms / Memory 13.9 MB
    def bestTeamScore_2(self, scores, ages):
        people = []
        for idx, score in enumerate(scores):
            people.append((score,ages[idx]))
        people.sort(key = lambda s: (s[0], s[1]) ) #多重排序
        
        dp = [0]*( max(ages) ) #idx取代age
        for p in people:
            (score, age) = p
            print(p)
            dp[age-1] = score + max(dp[:age])
        
        return max(dp)