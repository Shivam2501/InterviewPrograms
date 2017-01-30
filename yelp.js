function getElementsByClassName(className) {
    var list=[];
    var root=document.documentElement;
    function returnnode(node){
        var container=[];
        if(node.classList.contains(className)){
             list.push(node);
         }
         for(var i=0; i<node.children.length; i++){
             returnnode(node.children[i]);
         }
     }
    returnnode(root);
    return list;
}