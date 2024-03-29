class Solution {
public:
    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        int n = scores.size();
        int ans = 0;
        vector<int> dp(n,0); //1-D array
        vector<pair<int, int>> players; //2-D array
        
        // create sort age:score
        for(int i = 0; i < n; i++) 
            players.push_back({ages[i], scores[i]});
        
        sort(players.begin(), players.end());
        
        // DP 2 loop
        for(int i=0; i<n; i++) {
            dp[i] = players[i].second; //score
            for(int j = 0; j<i; j++) {
                // j<i && score[j]<=score[i]
                if(players[i].second >= players[j].second) { dp[i] = max(dp[i], dp[j] + players[i].second); }
            }
            ans = max(ans, dp[i]);
        }
        return ans;
    }
};