/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    var dfs = (left,right,s) => {
        if (s.length == n*2) {
            res.push(s)
            return
        }

        if (left < n) {
            dfs(left+1,right,s+'(')
        }
        if (left > right) {
            dfs(left,right+1,s+')')
        }
    }

    res = []
    dfs(0,0,'')
    return res
};

// Runtime 117 ms / Memory 43.8 MB
// debug: https://jsfiddle.net/