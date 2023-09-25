class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        sort(stones.begin(),stones.end()); //sort
        while (stones.size()>=2) {
            // get two largest stone
            int y = stones.back(); stones.pop_back();
            int x = stones.back(); stones.pop_back();
            // y > x , push_back
            if (x!=y) { stones.push_back(y-x); }
            // sort again
            sort(stones.begin(),stones.end());
        }
        // residue
        if (stones.size()==1) { return stones[0]; }
        else { return 0; }
    }
};