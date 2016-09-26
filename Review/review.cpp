#include <iostream>
#include <map>
#include <list>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<string> &split(const string &s, char delim, vector<string> &elems) {
   stringstream ss(s);
   string item;
    while (getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

vector<string> split(const string &s, char delim) {
   vector<string> elems;
    split(s, delim, elems);
    return elems;
}

int main() {

string instr[100],str;
ifstream file("reviewfile.txt");

int j=0;
while(std::getline(file,str)){
	instr[j]=str;
	j++;
}
map <string,list<int> > mymap;

for(int i=0;i<=j;i++){
	string word;
	vector<string> x = split(instr[i], ' ');
	for (vector<string>::iterator it = x.begin() ; it != x.end(); ++it){
  		mymap[*it].push_back(i);
	}
}
string input;

cout<<"Enter the word: ";
cin>>input;

for (list<int>::iterator it1=mymap[input].begin(); it1 != mymap[input].end(); ++it1)
    		cout << ' ' << instr[*it1]<<endl;


}