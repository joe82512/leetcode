/**
 * @param {number} rowIndex
 * @return {number[]}
 */
function factorialize(num) {
    if(num == 1 || num === 0){
        return 1
    }
    else{
        return (num * factorialize(num-1));
    }
}
function combination(n,m) {
    return factorialize(n)/(factorialize(m)*factorialize(n-m))
}

var getRow = function(rowIndex) {
    var prev = []
    for (i=0;i<=rowIndex;i++) {
        prev.push(combination(rowIndex,i))
    }
    return prev
};

// Runtime 106 ms / Memory 42.2 MB
// debug: https://jsfiddle.net/