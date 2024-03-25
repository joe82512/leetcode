class Solution {
public:
    string addBinary(string a, string b) {
        string res = "";
        int sum = 0;
        int curry = 0;
        int bitA = 0;
        int bitB = 0;
        int lenA = a.size();
        int lenB = b.size();

        while (lenA>0 | lenB>0 | curry>0) {
            bitA = (lenA>0) ? a[lenA-1]-'0' : 0; //ascii
            bitB = (lenB>0) ? b[lenB-1]-'0' : 0;
            sum = bitA + bitB + curry;
            res = to_string(sum%2) + res; //取餘

            curry = sum / 2; //取整
            lenA--; //shift
            lenB--;
        }

        return res;
    }
};