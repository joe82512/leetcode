/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let [s_arr, t_arr] = [s.split('').sort(), t.split('').sort()]
    return s_arr.join('') === t_arr.join('')
};

// Runtime 201 ms / Memory 49.3 MB
// debug: https://jsfiddle.net/