/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    var nums = nums1.concat(nums2);
    nums.sort((a,b)=>a-b);
    if (nums.length%2==0) {
        var n = [nums.length/2-1,nums.length/2];
    }
    else {
        var n = [(nums.length-1)/2,(nums.length-1)/2];
    }    
    result = nums[n[0]]+nums[n[1]];
    return result/2
};

// Runtime 181 ms / Memory 47.8 MB
// debug: https://jsfiddle.net/