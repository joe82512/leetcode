/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
 var removeElement = function(nums, val) {
    for (i=nums.length;i>=0;i--) {
        if (nums[i]==val) {
            nums.splice(i, 1)
            // 用delete會殘留undefined
        }
    }
    return nums.length
};

// Runtime 94 ms / Memory 42.4 MB
// debug: https://jsfiddle.net/