class Solution {
public:
    int titleToNumber(string columnTitle) {
        int r = 0;
        for (auto c:columnTitle) {
            int ascii = int(c-'A')+1; //char->ascii
            r = r*26 + ascii; //carry
        }
        return r;
    }
};