//Given a list of words, group all the anagrams. 
#include <iostream>
#include <utility>
#include <list>

using namespace std;

int main() {

string s[5];
list <pair<string,int> > mylist;

for(int i=0;i<5;i++){
	cin>>s[i];
}

string c[5];

for(int i=0;i<5;i++){
	c[i]=s[i];
}

for(int i=0;i<5;i++){
	sort(c[i].begin(),c[i].end());	//sort each word
	pair<string,int> p(c[i],i);
	mylist.push_back(p);
}
mylist.sort();	//sort the array

for(std::list<pair<string,int> >::iterator it=mylist.begin(); it!=mylist.end(); ++it){
	pair<string,int> p=*it;
	cout<<s[p.second];
}


}