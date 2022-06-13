/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    if (x < 0) {
        return false
    }
    else {
        x = String(x)
        return x == x.split("").reverse().join("")
    }
};

// Runtime 310 ms / Memory 51.4 MB
// debug: https://jsfiddle.net/