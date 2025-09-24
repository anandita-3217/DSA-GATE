#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node* left;
    struct Node* right;
} Node;

Node* createNode(int data){
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode -> data = data;
    newNode -> left = NULL;
    newNode -> right = NULL;
    return newNode;
}
void insert(Node** root, int data){
    if(*root == NULL){
        *root = createNode(data);
        return;
    }
    if (data<(*root) -> data){
        insert(&((*root)->left),data);
    }
    else if (data>(*root) -> data){
        insert(&((*root)->right),data);
        
    }
    
}
Node* findMin(Node* root){
    if (root&& root-> left != NULL){
        root = root -> left;
    }
    return root;

}
Node* findMax(Node* root){
    if (root&& root-> right != NULL){
        root = root -> right;
    }
    return root;

}
Node* delete(Node* root, int data){
    if (root == NULL){
        return root;
    }
    if (data<root->data){
        root -> left = delete(root->left,data);
    }
    else if (data>root->data){
        root -> right = delete(root->right,data);
    }
    else
    {
        if (root->left == NULL){
            Node* temp = root -> right;
            free(root);
            return temp;
        }
        else if (root->right == NULL){
            Node* temp = root -> left;
            free(root);
            return temp;
        }
        Node* temp = findMin(root->right);
        root -> data = temp->data;
        root->right = delete(root->right,temp->data);
    }
    return root;
}
Node* search(Node* root,int data){
    if (root == NULL || root->data == data){
        return root;
    }
    if(data < root->data){
        return search(root->left,data);
    }
    return search(root -> right,data);
    
}
