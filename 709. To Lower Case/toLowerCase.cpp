class Solution {
public:
    string toLowerCase(string s) {
        // transform(fist,last,result,op) , tolower is binary_op , use ::tolower
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        return s;
    }
};