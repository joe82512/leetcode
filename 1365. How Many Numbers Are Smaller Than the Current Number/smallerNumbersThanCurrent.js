/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    sr_nums = [...nums]
    sr_nums.sort((a,b) => a-b)
    result = []
    nums.forEach((n) => {
        result.push(sr_nums.indexOf(n))
    })
    return result
};

// Runtime 104 ms / Memory 44.2 MB
// debug: https://jsfiddle.net/