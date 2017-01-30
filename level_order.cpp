void printTree(Node* n) {
queue q;
q.enqueue(n); //push root node in the queue
int count_curr=1;
int count_next=0;

while(!q.isEmpty()){
    Node *temp=q.dequeue();
    count_curr--;
    if(temp!=NULL){
        print(temp->data);
        q.enqueue(temp->left);
        q.enqueue(temp->right);
        if(temp->left!=NULL){
            count_next++; 
        }
        if(temp->right!=NULL){
            count_next++;
            }
        }
        if(count_curr==0){
            cout<<endl;
            count_curr=count_next;
            count_next=0;
        }
        
        
   }

}
