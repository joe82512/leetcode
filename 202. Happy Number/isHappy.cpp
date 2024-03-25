class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> visit;
        
        int temp, t;
        while (n!=1) {
            temp = 0;
            while (n!=0) {
                t = n%10;
                n = n/10;
                temp = temp + t*t;
            }

            n = temp;
            if (visit.count(n)==1) { return false; } //loop number
            else { visit.insert(n); }
        }
        return true;
    }
};