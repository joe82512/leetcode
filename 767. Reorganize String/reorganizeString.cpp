class Solution {
public:
    string reorganizeString(string s) {
        string res = "";
        unordered_map<char, int> cnt;
        priority_queue<pair<int, char>> heap;
        for (char c:s) { cnt[c]++; }
        for (auto a:cnt) {
            // 數量超過一半 , 必為空
            if ( a.second > (s.length()+1)/2 ) { return ""; }
            // else
            heap.push({a.second, a.first});
        }
        // 填充
        while (heap.size() >= 2) {
            // heap 取出
            auto t1 = heap.top(); heap.pop();
            res.push_back(t1.second);
            auto t2 = heap.top(); heap.pop();
            res.push_back(t2.second);
            // 若數量仍足夠, 放回 heap
            if (t1.first > 1) { t1.first--; heap.push(t1); }
            if (t2.first > 1) { t2.first--; heap.push(t2); }
        }
        // 奇數 , 最後一個
        if (heap.size() > 0) { res.push_back(heap.top().second); }
        
        return res;
    }
};