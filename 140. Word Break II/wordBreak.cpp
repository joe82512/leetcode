class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_map<string, vector<string>> table;
        vector<string> output;
        output = DFS(s, wordDict, table);
        /* show hashmap
        for (const auto& n:table) {
            cout << n.first << ":";
            for (const auto& v:n.second) { cout << v << " "; }
            cout << endl;
        }
        */
        return output;
    }

    // table {catsanddog: [cat sand dog cats and dog], anddog: [and dog], sanddog: [sand dog], dog: [dog]}
    vector<string> DFS(string s, vector<string>& wordDict, unordered_map<string, vector<string>>& table) {
        //already used, continue
        if (table.count(s)) { return table[s]; }
        //end word
        if (s.empty()) { return {""}; }
        vector<string> res;
        for (string word : wordDict) {
            // word != s[0:len(word)]
            if (s.substr(0, word.size()) != word) { continue; }
            // else : DFS(s[len(word):],wordDict,table)
            vector<string> rem = DFS(s.substr(word.size()), wordDict, table);
            //create list
            for (string str : rem) {
                //combine: str.empty check end word
                res.push_back(word + (str.empty() ? "" : " ") + str);
            }
        }
        table[s] = res;
        return res;
    }
};

/*
    s:  cat -> sanddog
    s:  sand -> dog
    s:  dog -> 
    rem:  ['']
    **** DFS res: ['dog ']
    rem:  ['dog ']
    **** DFS res: ['sand dog ']
    rem:  ['sand dog ']
    s:  cats -> anddog
    s:  and -> dog
    rem:  ['dog ']
    **** DFS res: ['and dog ']
    rem:  ['and dog ']
    **** DFS res: ['cat sand dog ', 'cats and dog ']
    => table: {
        'dog': ['dog '],
        'sanddog': ['sand dog '],
        'anddog': ['and dog '],
        'catsanddog': ['cat sand dog ', 'cats and dog ']
    }
*/