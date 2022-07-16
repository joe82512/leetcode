/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    var shift = 0
    const n = nums.length //must define
    for (let i=0;i<n;i++){
        if (nums[i-shift]==0){
            nums.splice(i-shift,1)
            shift += 1
        }
    }
    // var arr = new Array(counts)
    // arr.fill(0)
    // nums = nums.concat(arr) //leetcode failed
    for (let i=0;i<shift;i++){
        nums.push(0)
    }    
};

// Runtime 161 ms / Memory 46.8 MB
// debug: https://jsfiddle.net/