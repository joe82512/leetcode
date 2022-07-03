/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 var subsets = function(nums) {
    result = []
    DFS(nums, [] , result)
    return result
};

function DFS(nums, path, result) {
    result.push(path)
    for (let i=0; i<nums.length; i++) { //i must let
        DFS(nums.slice(i+1),[...path,nums[i]],result)
    }
}

// Runtime 90 ms / Memory 44.8 MB
// debug: https://jsfiddle.net/