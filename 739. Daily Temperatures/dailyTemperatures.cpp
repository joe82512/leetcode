class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        stack<int> st; //record small index in Right
        vector<int> output(n,0);

        for (int i=0; i<n; i++) {
            while (!st.empty()) {
                int now = st.top();
                // continue pop(-1) if large
                if (temperatures[i] > temperatures[now]) {
                    output[now] = i - now;
                    st.pop();
                }
                // not pop and break, st must record if small
                else { break; }
            }
            st.push(i); //append record
        }

        return output;
    }
};