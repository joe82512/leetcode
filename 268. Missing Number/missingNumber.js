/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    var sort_nums = []
    for (let i=0; i<=nums.length; i++) {
        sort_nums.push(i)
    }
    let set_sort_nums = new Set(sort_nums)
    let set_nums = new Set(nums)
    let diff= new Array([...set_sort_nums].filter(x=>!set_nums.has(x)))
    return diff
};

// Runtime 75 ms / Memory 51.8 MB
// debug: https://jsfiddle.net/