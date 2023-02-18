class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        vector<int> charMap(26); //new idx
        for (int i = 0; i < order.size(); i++) {
            //int idx = order[i] - 'a'; //ASCII to int
            //cout << idx << endl;
            charMap[order[i] - 'a'] = i;
        }
        for (string &word : words) {
            for (char &c : word) {
                //cout << c << endl; //ASCII
                c = charMap[c - 'a'];
                //cout << int(c) << endl; //ASCII to int
            }
        }
        return is_sorted(words.begin(), words.end());
    }
};