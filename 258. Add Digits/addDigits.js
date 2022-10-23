/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    while (num>9) {
        var r = 0
        let num_str = num.toString();
        for (i=0;i<num_str.length;i++) {
            r = r + parseInt(num_str[i])
        }
        num = r
    }
    return num
};

// Runtime 128 ms / Memory 44.2 MB
// debug: https://jsfiddle.net/