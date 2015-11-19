#include <stack>
#include <iostream>
#include <string>
#include <utility>
#include <map>

using namespace std;

int main() {

string para,out;

cout<<"Enter the string: ";
cin>>para;
pair<char,int> p;
stack<pair<char,int> > key;
map<int,bool> check;

int i=0;
while(i<para.length()){

	if(para.at(i)=='('){
		pair<char,int> p(para.at(i),i);
		key.push(p);
		check[i]=false;
	}

	else if(para.at(i)==')'){
		if(key.empty()){
			check[i]=false;
		}
		else{
			p=key.top();
			key.pop();
			check[i]=true;
			check[p.second]=true;
		}
	}

	i++;
}

i=0;
while(i<para.length()){
	if(check[i]==true){
		out += para.at(i);
	}
	i++;
}
cout<<"The output is: "<<out<<endl;
return 0;
}