/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    var comb = (can,tar,res,res_list) => {
        if (tar==0) {
            res_list.push([...res])
            return
        }
        else if (tar>0) {
            // [...res, can[i]] not res+[can[i]]
            // res+[can[i]] : [3,12] -> [3,1,2]
            for (let i=0; i<can.length; i++) {
                comb(can.slice(i), tar-can[i], res+[can[i]], res_list)
            }
        }
        else {
            return
        }
    }

    res_list = []
    comb(candidates,target,[],res_list)
    return res_list
};

// Runtime 145 ms / Memory 48.5 MB
// debug: https://jsfiddle.net/