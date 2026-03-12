//question number 795

class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {

        int count = 0;
        int maxi = -1;  
        int id = -1;    

        for (int i = 0; i < nums.size(); i++) {

            if (nums[i] > right) {
                maxi = i;
            }

            if (nums[i] >= left) {
                id = i;
            }

            if (id > maxi) {
                count += id - maxi;
            }
        }

        return count;
    }
};
