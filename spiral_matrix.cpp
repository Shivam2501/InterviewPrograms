#include <iostream>
using namespace std;


/*
 * Given a NxN grid of sequential numbers, e.g. N=3
 * 1 2 3
 * 4 5 6
 * 7 8 9
 *
 * Print the numbers in a spiral pattern starting
 * from the top left and ending in the middle
 *
 * For N=3, print: 1 2 3 6 9 8 7 4 5
 *
 * For N=2,
 * 1 2
 * 3 4
 *
 * print: 1 2 4 3
 *
 * For N=4,
 * 1 2 3 4
 * 5 6 7 8
 * 9 10 11 12
 * 13 14 15 16
 *
 * print: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
 */


void spiral(int n) {
  
  int k=0, l=0;
  int a[n][n],counter=1;
  int m=n;
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      a[i][j]=counter;
      counter++;
    }
  }
  while(k<m && l<n){
    //first row
    for(int i=l;i<n;++i){
      cout<<a[k][i];
    }
    k++;
    
    //last column
    for(int i=k;i<m;++i){
      cout<<a[i][n-1];
    }
    n--;
    
    //last row
    if(k<m){
      for(int i=n-1;i>=l;--i){
        cout<<a[m-1][i];
      }
      m--;
    }
    
    //first column
    if(l<n){
      for(int i=m-1;i>=k;--i){
        cout<<a[i][l];
      }
      l++;
    }
  }
}


// To execute C++, please define "int main()"
int main() {
  // auto words = { "Hello, ", "World!", "\n" };
  // for (const auto& word : words) {
  //   cout << word;
  // }
  
  spiral(1);
  
  return 0;
}

