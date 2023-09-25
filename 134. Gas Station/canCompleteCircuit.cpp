class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total = 0; //run all
        int temp = 0;
        int station = 0;
        for (int i=0; i<gas.size(); i++) {
            int diff = gas[i]-cost[i];
            total += diff;
            temp += diff;
            // not complete
            if (temp < 0) {
                temp = 0;
                station = i+1; //start at next station
            }
        }
        if (total >= 0) { return station; } //impossible
        else { return -1; }
    }
};