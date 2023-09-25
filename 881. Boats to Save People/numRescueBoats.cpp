class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(),people.end());
        int L = 0, R = people.size()-1;
        int boats = 0;
        while (L<=R) {
            // pair
            if (people[L]+people[R] <= limit) {
                L++; R--;
            }
            // cant pair
            else { R--; }
            // cnt
            boats++;
        }
        return boats;
    }
};