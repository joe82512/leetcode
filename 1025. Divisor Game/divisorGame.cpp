class Solution {
public:
    bool divisorGame(int n) {
        /*
        GOAL : grab even number
        just always choose 1
        if n odd
            A : odd -> even
            B : even -> odd
            loop ---> B get 2
        */
        return (n%2==0);
    }
};