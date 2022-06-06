/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
 var findTheDifference = function(s, t) {    
    const st = s + t
    let result = st[0].charCodeAt(0) // ord()
    for (i=1;i<st.length;i++) {
        result ^= st[i].charCodeAt(0) // ord()
    }
    return String.fromCharCode(result) // chr()
};

// Runtime 60 ms / Memory 42.4 MB
// debug: https://jsfiddle.net/