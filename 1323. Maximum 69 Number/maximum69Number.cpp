class Solution {
public:
    int maximum69Number (int num) {
        stack<int> st;
        int r = 0;
        int res = 0;
        bool change = false;
        // get value as vector
        while (num) {
            st.push(num%10);
            num = num/10;
        }
        // change first 6 to 9
        while (!st.empty()) {
            // first 6
            if (st.top()==6 and !change) {
                r = 9;
                change = true;
            }
            // 
            else {
                r = st.top();
            }
            st.pop();
            // recover value
            res = res*10 + r;
        }
        return res;
    }
};