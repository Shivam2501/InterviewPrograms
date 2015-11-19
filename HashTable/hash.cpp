/*
This is a program which implements a fixed-size hash map associating string keys with arbitrary data object refrences.
A simple hashing function which returns the length of the string is used to find the index. Separate chaining with linked list
is used as a method for collision handling. This means each slot in the hash table contains a linked list.

Set: Inserting the value is done at the head of the linked list to guarantee the constant inserting time O(1).
Get and Delete: Parse the linked list to find the node with the given key and return it. Worst case running time is O(n).

Author: Shivam Bharuka
Email: bharuka2@illinois.edu
*/

#include <iostream>
#include <string>
#include <utility>
using namespace std;
const int size=100;

class Linkedlist{	
	public:
	pair<string,int> p;    // tuple to store key and value in the hash table
	Linkedlist *next;      
	Linkedlist(string key,int value){   //constructor
		p.first=key;
		p.second=value;
		this->next=NULL;
	}
};

class HashTable{
private:
	Linkedlist **table;
	int count;			//count of the elements inserted in the linked list
public:
	HashTable(){		//constructor 
		table=new Linkedlist *[size];
		for(int i=0;i<size;i++){
			table[i]=NULL;
		}
		count=0;
	}
	bool set(string key,int value); //store an element
	bool check(string key); //check if the key exists in the table
	int get(string key);	//return the value associated with a given key
	int pop(string key);	//delete the value associated with a given key
	int function(string key); // hash function
	float load();		// calculuate load factor
	~HashTable(){		//destructor to free the memory
		for(int i=0;i<size;i++){
			if(table[i]!=NULL)
				delete table[i];
			delete[] table;
		}
	}
};

int HashTable::function(string key){  //hash function reutrns the length of the string
	return key.length();
}

bool HashTable::set(string key, int value){  //store an element
	int index=function(key);		//call hash function to find the index
	Linkedlist *curr= table[index];  //head of the list 
	while(curr!=NULL){			//check if already exists
		if(curr->p.first==key){
			curr->p.second=value;		//if yes then update
			return true;
		}
		curr=curr->next;
	}
	curr=new Linkedlist(key,value);		//create a new node
	curr->next=table[index];    
	table[index]=curr;	
	count++;		//increment count as node is added
	return true;
}
bool HashTable::check(string key){ //check if the key exists in the table
 int find=function(key);   //call hash function to find the index
	Linkedlist *curr= table[find];	//head of the list 
	while(curr!=NULL){		//check if already exists
		if(curr->p.first==key){
			return true;		//if yes then return true
		}
		curr=curr->next;
	}
	return false;
}

int HashTable::get(string key){
	int find=function(key);		//call hash function to find the index
	Linkedlist *curr= table[find];	//head of the list 
	while(curr!=NULL){
		if(curr->p.first==key){
			return curr->p.second;	
		}
		curr=curr->next;
	}
	return 0;
}
int HashTable::pop(string key){
	int find=function(key);		//call hash function to find the index
	Linkedlist *temp;

	if(table[find]==NULL){			//if empty return NULL
		return 0;
	}

	if(table[find]->p.first==key){		//if head has the same key
		temp=table[find];
		int value=table[find]->p.second;
		table[find]=temp->next;
		delete temp;
		count--;	//decrement count as deleting the node
		return value;
	}

	Linkedlist *curr=table[find];
	while(curr->next!=NULL){
		if(curr->next->p.first==key){
			temp=curr->next;
			int value=curr->next->p.second;
			curr->next=temp->next;
			delete temp;
			count--;	//decrement count as deleting the node
			return value;
		}
		curr=curr->next;
	}

	return 0;
}
float HashTable::load(){
	return (float)count/(float)size;	//calculate load factor after casting int to float
}
int main(){
	HashTable hash;
	string key;
	int value,choice,out;
	while(1){
		cout<<"1. Insert element into the table"<<endl;
        cout<<"2. Search element from the key"<<endl;
        cout<<"3. Delete element at a key"<<endl;
        cout<<"4. Load factor"<<endl;
        cout<<"Any other key to exit"<<endl;
        cout<<"Enter your choice: ";
        cin>>choice;
        switch(choice)
        {
        	case 1: cout<<"Enter the key: ";	
        			cin>>key;
        			cout<<"Enter the value: ";
        			cin>>value;
        			if(hash.set(key,value)==true)
        				cout<<"Value Stored!"<<endl;
        			break;

        	case 2: cout<<"Enter the key: ";	
        			cin>>key;
        			if(hash.check(key)==true){		//check if key exists in the table
        				out=hash.get(key);
        				cout<<"The value is: "<<out<<endl;
        			}
        			else
        			   cout<<"The key doesn't exists."<<endl;
        			break;

        	case 3: cout<<"Enter the key: ";	
        			cin>>key;
        			if(hash.check(key)==true){		//check if key exists in the table
        				out=hash.pop(key);
        				cout<<"The value is: "<<out<<endl;
        			}
        			else
        				cout<<"The key doesn't exists."<<endl;
        			break;

        	case 4: cout<<"Load factor is: "<<hash.load()<<endl;
        			break;

        	default:exit(1);
        }
	}
	return 0;
}

