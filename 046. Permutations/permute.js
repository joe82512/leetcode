/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    var dfs = (nums,path,res) => {
        if (nums.length==0) {
            res.push([...path]) //must [...path]
            return
        }
        else {
            const len = nums.length
            for (let i=0;i<len;i++) {
            // for (let num of nums) {
                path.push(nums[i])
                new_nums = nums.slice(0,i).concat(nums.slice(i+1))
                // new_nums = nums.filter(item => item !== nums[i])
                dfs(new_nums,path,res)
                path.pop()
            }
        }
    }
    
    res = []
    dfs(nums,[],res)
    return res
};

// Runtime 125 ms / Memory 44.7 MB
// debug: https://jsfiddle.net/