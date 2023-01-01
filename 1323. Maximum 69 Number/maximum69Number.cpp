class Solution {
public:
    int maximum69Number (int num) {
        stack<int> s;
        int r = 0;
        int res = 0;
        bool change = false;
        while (num) {
            s.push(num%10);
            num = num/10;
        }
        while (!s.empty()) {
            if (s.top()==6 and !change) {
                r = 9;
                change = true;
            }
            else {
                r = s.top();
            }
            res = res*10 + r;
            s.pop();
        }
        return res;
    }
};