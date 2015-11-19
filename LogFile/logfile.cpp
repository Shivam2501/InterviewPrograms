
#include <stack>
#include <iostream>
#include <utility>
#include <map>
#include <list>
#include <fstream>

using namespace std;

int main() {

string instr[100],str;
std::ifstream file("logfile.txt");

int j=0;
while(std::getline(file,str)){
	instr[j]=str;
	j++;
}

map<string,int> mymap;
list<pair<int,string> > mylist;

for(int i=0;i<j;i++){
		mymap[instr[i]]++;
}
	
for (std::map<string,int>::iterator it=mymap.begin(); it!=mymap.end(); ++it){
	pair<int,string> p(it->second,it->first);
	mylist.push_back(p);
}

mylist.sort();
for(std::list<pair<int,string> >::reverse_iterator it=mylist.rbegin(); it!=mylist.rend(); ++it){
	for(int i=0;i<10;i++){
		pair<int,string> p=*it;
		cout<<"URL: "<<p.second<<" Count: "<<p.first<<endl;
	}
}

}