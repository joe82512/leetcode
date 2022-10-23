/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const words = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    
    var dfs = (nums,path,res) => {
        if (nums == digits.length) {
            res.push(path.join(''))
            return
        }
        else {
            next_number = digits[nums]
            let word =  words[next_number] //must define let   
            for (let i=0;i<word.length;i++) { // for (let w of word)
                path.push(word[i]) // path.push(w)
                dfs(nums+1,path,res)
                path.pop()
            }
            
        }
    }
    
    if (digits.length==0) {return []}        
    else {
        res=[]
        dfs(0,[],res)
        return res
    }
};

// Runtime 65 ms / Memory 41.6 MB
// debug: https://jsfiddle.net/