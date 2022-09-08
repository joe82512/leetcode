/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    a = nums[0]
    if (nums.length===1) {
        return a
    }
    else {
        b = Math.max(nums[0],nums[1])
        nums.slice(2).forEach(n => {
            [b,a] = [Math.max(a+n,b),b]
        });
        return b
    }
};

// Runtime 88 ms / Memory 42.2 MB
// debug: https://jsfiddle.net/