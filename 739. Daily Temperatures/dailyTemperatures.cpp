class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack <int> st;
        vector <int> res(temperatures.size());

        for (int i=0; i<temperatures.size(); i++) {
            while (!st.empty()) {
                int last = st.top();
                if (temperatures[i] > temperatures[last]) {
                    res[last] = i - last;
                    st.pop();
                }
                else {
                    break;
                }
            }
            st.push(i);
        }
        return res;
    }
};