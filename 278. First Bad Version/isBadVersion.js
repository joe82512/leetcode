/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        if (n==1) {
            return n
        }
        else {
            left = 1
            right = n
            while (left < right) {
                let mid = Math.floor((left+right)/2)
                if (mid==left) {
                    if (isBadVersion(left)) {
                        return left
                    }
                    else {
                        return right
                    }
                }
                else {
                    if (isBadVersion(mid)) {
                        right = mid
                    }
                    else {
                        left = mid
                    }
                }
            }
        }
    };
};

// Runtime 82 ms / Memory 42 MB
// debug: https://jsfiddle.net/