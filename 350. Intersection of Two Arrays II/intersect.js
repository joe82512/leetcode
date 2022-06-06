/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
 var intersect = function(nums1, nums2) {
    nums1.sort((a,b) => a-b) // sort by number
    nums2.sort((a,b) => a-b) // sort by number
    let hash_map = new Map()
    i = 0
    j = 0
    while (i<nums1.length && j<nums2.length) {
        if (nums1[i]==nums2[j]) {
            hash_map.set(i, nums1[i])
            i++
            j++
        }
        else if (nums1[i]<nums2[j]) {
            i++
        }
        else {
            j++
        }
    }
    return [...hash_map.values()]
};

// Runtime 95 ms / Memory 43.6 MB
// debug: https://jsfiddle.net/