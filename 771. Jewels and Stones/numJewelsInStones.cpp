class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int cnt = 0;
        for (auto jewel:jewels) { //class
            for (auto stone:stones) { //items
                if (jewel==stone) { cnt++; }
            }
        }
        return cnt;
    }
};