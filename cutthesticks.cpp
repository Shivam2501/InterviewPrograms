#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> cutsticks(vector<int> input){
	sort(input.begin(), input.end());

	vector<int> result;
	result.push_back(input.size());
	int min = input[0];
	int counter = input.size();
	for(unsigned int i = 0; i < input.size(); i++){
		if(input[i] - min != 0){
			result.push_back(counter);
			min = input[i];
		}
		counter--;
	}
	return result;
}

int main(){

	vector<int> example;
	example.push_back(1);
	example.push_back(1);
	example.push_back(4);
	example.push_back(3);
	example.push_back(6);
	example.push_back(6);
	example.push_back(4);
	example.push_back(1);
	vector<int> out = cutsticks(example);
	for(int i = 0; i < out.size(); i++){
		cout << out[i] << endl;
	}
	return 0;
}