/**
 * @param {number[]} nums
 * @return {number}
 */
 var intersection = function(nums1, nums2) {
    const nums1_set = new Set(nums1)
    const nums2_set = new Set(nums2)
    const intersect = new Set([...nums1_set].filter(x=>nums2_set.has(x)))
    return [...intersect] //cant submit set type
};

// Runtime 79 ms / Memory 43.8 MB
// debug: https://jsfiddle.net/