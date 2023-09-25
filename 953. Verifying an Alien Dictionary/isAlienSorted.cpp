class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        vector<int> charMap(26); //new idx
        for (int i = 0; i < order.length(); i++) {
            //int idx = order[i] - 'a'; //ASCII to int
            //cout << idx << endl;
            charMap[order[i] - 'a'] = i;
        }
        for (string &word : words) {
            for (char &c : word) {
                //cout << int(c) << endl; //ASCII to int
                c = charMap[c - 'a']; //ref c
            }
        }
        return is_sorted(words.begin(), words.end());
    }
};