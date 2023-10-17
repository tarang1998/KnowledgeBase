class Solution {
    
public:

    // Time Complexity : O(n*m)
    // Space Complexity : O(n+m)
    void setZeroes(vector<vector<int>>& matrix) {

        int n = matrix.size();
        int m = matrix[0].size();

        unordered_set<int> rowsToBeSetToZero;
        unordered_set<int> columnsToBeSetZero;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(matrix[i][j] == 0 ){
                    rowsToBeSetToZero.insert(i);
                    columnsToBeSetZero.insert(j);
                }

            }
        }


        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(rowsToBeSetToZero.contains(i)){
                    matrix[i][j] = 0;
                }
                if(columnsToBeSetZero.contains(j)){
                    matrix[i][j] = 0;
                }
                

            }
        }
   
        
    }
};