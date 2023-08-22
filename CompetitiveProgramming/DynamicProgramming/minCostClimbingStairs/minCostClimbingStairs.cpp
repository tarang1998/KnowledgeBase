
using namespace std;

class Solution {
public:

    int minCostClimbingStairs(vector<int>& cost) {

        int dp0 = cost[0];

        int dp1 = cost[1];

        for(int i = 2; i< cost.size() ;i++){

            int curr = cost[i] + std::min(dp0,dp1);

            dp0 = dp1;

            dp1 = curr;

        }

        return std::min(dp0,dp1);
        
    }
};