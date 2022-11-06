/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    var group = {}
    for (let str of strs) {
        let sort_str = [...str].sort().join('')
        if (sort_str in group) {
            group[sort_str].push(str);
        }
        else {
            group[sort_str] = [str]
        }
    }
    return Object.values(group);
};

// Runtime 196 ms / Memory 53 MB
// debug: https://jsfiddle.net/