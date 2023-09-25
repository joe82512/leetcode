class Solution {
public:
    string toHex(int num) {
        if(num == 0) { return "0"; }
        
        unsigned int n = num; //neg->pos
        
        string hex_map = "0123456789abcdef";
        string output = "";
        while (n>0) {
            int idx = n % 16;
            output = hex_map[idx] + output; //add front
            n = n/16;
        }
        return output;
    }
};