class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int n_ransomNote = ransomNote.length();
        int n_magazine = magazine.length();
        // char not enough
        if (n_ransomNote>n_magazine) { return false; }
        // else : two pointer
        sort(ransomNote.begin(), ransomNote.end());
        sort(magazine.begin(), magazine.end());
        int i=0, j=0;
        while (i<n_ransomNote && j<n_magazine) {
            if (ransomNote[i] == magazine[j]) { i++; j++; } //same
            else { j++; }
        }
        return (i==n_ransomNote); //goto end
    }
};