/*
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int>::iterator temp1,temp2;
        for(std::vector<int>::iterator it=nums.begin();it!=nums.end();++it){
            temp1=it;
            for(std::vector<int>::iterator j=temp1+1;j!=nums.end();j++){
                temp2=j;
                if(*temp1+*j==target){
                    vector<int> answer;
                    answer.push_back(std::distance(nums.begin(), temp1)+1);
                    answer.push_back(std::distance(nums.begin(), temp2)+1);
                    return answer;
                }
            }
        }
    }
};