class Solution {
public:
    int countOdds(int low, int high) {
        // extended range , ex : [3,5,7] => 3~7 or 2~8 
        if (low%2 == 0) { low++; }
        if (high%2 == 0) { high--; }
        // get interger
        return (high-low)/2+1;
    }
};