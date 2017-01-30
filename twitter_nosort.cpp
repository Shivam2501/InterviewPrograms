#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int main() {
  int N;
  vector<int> v;
  int temp = numeric_limits<int>::max();

  cin >> N;

  for(int i = 0; i < N; i++) {
    int num;
    cin >> num;
    v.push_back(num);

    if(num < temp)
      temp = num;
  }

  int sum = -1;
  int newsmall = temp;
  cout << v.size() << endl;

  while(sum != 0) {
    sum = 0;
    for(unsigned int i = 0; i < v.size(); i++) {
      v[i] -= temp;
      
      if(v[i] <= 0)
        continue;

      sum++;
      if(v[i] < newsmall)
        newsmall = v[i];
    }
    temp = numeric_limits<int>::max();
    for(unsigned int i = 0; i < v.size(); i++) {
      if(v[i] <= 0)
        continue;
      if(v[i] < temp)
        temp = v[i];
      //cout << v[i] << " ";
    }
    cout << endl;
    cout << "newsmall = " << newsmall << endl;
    // temp = newsmall;
    if(sum != 0)
    cout << sum << endl;
  }

  return 1;
}