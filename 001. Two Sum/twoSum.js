/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let result = [0,1]
    let hash_map = new Map() // better than object {}
    nums.forEach( (val, idx) => { // value,index
        if (!(hash_map.has(val))) {
        	hash_map.set(target-val, idx)
        }
        else {
            result = [hash_map.get(val), idx]
        }
    } )
    return result
};

// Runtime 69 ms / Memory 45.3 MB
// debug: https://jsfiddle.net/