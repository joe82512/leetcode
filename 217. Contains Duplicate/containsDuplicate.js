/**
 * @param {number[]} nums
 * @return {number}
 */
 var containsDuplicate = function(nums) {
    const nums_set = new Set(nums) //set
    const set_arr = [...nums_set] //turn array for length
    return set_arr.length !== nums.length
};

// Runtime 141 ms / Memory 50.6 MB
// debug: https://jsfiddle.net/