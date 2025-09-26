#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* left;
    struct Node* right;
} Node;

// Create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Insert a node into the BST
void insert(Node** root, int data) {
    if (*root == NULL) {
        *root = createNode(data);
        return;
    }
    
    if (data < (*root)->data) {
        insert(&((*root)->left), data);
    } else if (data > (*root)->data) {
        insert(&((*root)->right), data);
    }
    // If data equals root->data, we don't insert (no duplicates)
}

// Find the minimum value node in a tree
Node* findMin(Node* root) {
    while (root && root->left != NULL) {
        root = root->left;
    }
    return root;
}

// Delete a node from the BST
Node* delete(Node* root, int data) {
    if (root == NULL) {
        return root;
    }
    
    if (data < root->data) {
        root->left = delete(root->left, data);
    } else if (data > root->data) {
        root->right = delete(root->right, data);
    } else {
        // Node to be deleted found
        
        // Case 1: No child or only right child
        if (root->left == NULL) {
            Node* temp = root->right;
            free(root);
            return temp;
        }
        // Case 2: Only left child
        else if (root->right == NULL) {
            Node* temp = root->left;
            free(root);
            return temp;
        }
        
        // Case 3: Two children
        Node* temp = findMin(root->right);
        root->data = temp->data;
        root->right = delete(root->right, temp->data);
    }
    return root;
}

// Search for a value in the BST
Node* search(Node* root, int data) {
    if (root == NULL || root->data == data) {
        return root;
    }
    
    if (data < root->data) {
        return search(root->left, data);
    }
    
    return search(root->right, data);
}

// Inorder traversal (Left -> Root -> Right)
void inorder(Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

// Preorder traversal (Root -> Left -> Right)
void preorder(Node* root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

// Postorder traversal (Left -> Right -> Root)
void postorder(Node* root) {
    if (root != NULL) {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}

// Free all nodes in the tree
void freeTree(Node* root) {
    if (root != NULL) {
        freeTree(root->left);
        freeTree(root->right);
        free(root);
    }
}

// Main function to demonstrate usage
int main() {
    Node* root = NULL;
    
    // Insert nodes
    insert(&root, 50);
    insert(&root, 30);
    insert(&root, 70);
    insert(&root, 20);
    insert(&root, 40);
    insert(&root, 60);
    insert(&root, 80);
    
    printf("Inorder traversal: ");
    inorder(root);
    printf("\n");
    
    printf("Preorder traversal: ");
    preorder(root);
    printf("\n");
    
    printf("Postorder traversal: ");
    postorder(root);
    printf("\n");
    
    // Search for a value
    int searchValue = 40;
    Node* found = search(root, searchValue);
    if (found != NULL) {
        printf("Found %d in the tree\n", searchValue);
    } else {
        printf("%d not found in the tree\n", searchValue);
    }
    
    // Delete a node
    printf("Deleting 20...\n");
    root = delete(root, 20);
    printf("Inorder traversal after deletion: ");
    inorder(root);
    printf("\n");
    
    printf("Deleting 30...\n");
    root = delete(root, 30);
    printf("Inorder traversal after deletion: ");
    inorder(root);
    printf("\n");
    
    printf("Deleting 50...\n");
    root = delete(root, 50);
    printf("Inorder traversal after deletion: ");
    inorder(root);
    printf("\n");
    
    // Clean up memory
    freeTree(root);
    
    return 0;
}