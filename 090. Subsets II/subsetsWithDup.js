/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 var subsetsWithDup = function(nums) {
    nums.sort((a, b) => a-b)
    result = []
    DFS(nums, [] , result)
    return result
};

function DFS(nums, path, result) {
    result.push(path)
    for (let i=0; i<nums.length; i++) {
        if (i>0 & nums[i]==nums[i-1]) {
            continue
        }
        DFS(nums.slice(i+1),[...path,nums[i]],result)
    }
}

// Runtime 96 ms / Memory 44.4 MB
// debug: https://jsfiddle.net/