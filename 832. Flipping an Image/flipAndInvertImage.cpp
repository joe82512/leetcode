class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        int n = image.size();
        for (int i=0; i<n; i++) {
            for (int j=0; j<n/2; j++){ // n/2 int
                swap(image[i][j],image[i][n-j-1]); //Left <-> Right
                image[i][j] = 1^image[i][j]; // XOR: 1^b = ~b
                image[i][n-j-1] = 1^image[i][n-j-1];
            }
            // middle of odd row
            if (n%2==1) { image[i][n/2] = 1^image[i][n/2]; }
        }
        return image;
    }
};