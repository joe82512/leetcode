/**
 * @param {number} m
 * @param {number} n
 * @return {number}
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

var uniquePaths = function(m, n) {
    return combination(m+n-2,m-1)
};

// Runtime 62 ms / Memory 41.9 MB
// debug: https://jsfiddle.net/