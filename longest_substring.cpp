/*
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc"
, which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
*/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len=s.length();
        map<char,bool> str;
        int maximum=0,j=0;
        
        for(int i=0;i<s.length();i++){
            if(str[s.at(i)]){
                maximum=max(maximum,i-j);
                while(s.at(i)!=s.at(j)){
                    str[s.at(j)]=false;
                    j++;
                }
                j++;
            }
            else{
                str[s.at(i)]=true;
            }
        }
        j=s.length()-j;
        maximum=max(maximum,j);
        return maximum;
    }
    
};