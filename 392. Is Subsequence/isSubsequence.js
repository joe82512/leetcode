/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    if (s.length > t.length) {
        return false
    }
    else if (s.length===0) {
        return true
    }
    else {
        var c = 0
        for (i=0;i<t.length;i++) {
            if (s[c]===t[i]) {
                c += 1
            }
        }
        return c === s.length
    }
};

// Runtime 93 ms / Memory 42.1 MB
// debug: https://jsfiddle.net/