/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const sym = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    var v = []
    for (let i=0; i<s.length; i++) {
        sv = s[i]
        v.push(sym[sv])
    }
    var result = v[0]
    for (let i=1; i<s.length; i++) {
        result += v[i]
        if (v[i-1] < v[i]) {
            result -= v[i-1]*2
        }
    }
    return result
};

// Runtime 228 ms / Memory 47.8 MB
// debug: https://jsfiddle.net/