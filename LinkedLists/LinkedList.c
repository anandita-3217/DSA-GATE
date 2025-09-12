/*#include <stdio.h>
#include <stdlib.h>
typedef struct Node
{
    int data;
   struct Node * next;
} Node ;
Node* createNode(int data){
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL){
        printf("Memory allocation failed\n");
        exit(1);
    }
}
Node* insertAtBeginning(Node* head,int data){
    Node* newNode = createNode(data);
    // (*newNode).next = head;
    newNode->next = head;
    return newNode;
}
Node* insertAtEnd(Node* head, int data){
    Node* newNode = createNode(data);
    if (head == NULL){
        return newNode;
    }
    Node* temp = head;
    while(newNode != NULL){
        temp = temp -> next;
    }
    temp->next = newNode;
    return head;
}
Node* insertAtposition(Node* head,int data,int position){
    if (position<0){
        printf("Position cannt be negative");
        return head;
    }
    if (position==0){
        return insertAtBeginning(head,data);
    }
    Node* newNode = createNode(data);
    Node* temp = head;
    for (int i = 0; i < position-1&& temp != NULL; i++)
    {
        temp = temp -> next;
    }
    if (temp==NULL){
        printf("Index Out of Bounds");
        free(newNode);
        return head;
    }
    newNode->next = temp->next;
    temp->next = newNode;
    return head;
}
void traversalList(Node* head){
    printf("Travesing Linked list");
    if(head == NULL){
        printf("Linked List is empty");
        return;
    }
    Node* current = head;
    while (current != NULL)
    {
        printf("%d ",current->data);
        current = current->next;
    }
    printf("\n");
    
}
int countNodes(Node* head){
    printf("Counting Nodes");
    int count  = 0;
    Node* current = head;
    while (current != NULL)
    {
        count++;
        current = current->next;
    }
    return count;
}
Node* deleteByValue(Node* head,int value){
    if (head == NULL){
        return NULL;
    }
    if (head->data = value)
    {
        Node* temp = head;
        head= head -> next;
        free(temp);
        return head;
    }
    Node* current = head;
    while (current->next != NULL && current->next->data != value)
    {
        current = current->next;
    }
    if(current->next!=NULL){
        Node* temp= current->next;
        current->next = current->next->next;
        free(temp);
    }
    
    return head;
}
Node* deleteByPosition(Node* head,int position){
    if (head == NULL||position<0) return NULL;
    Node* current = head;
    if(position == 0){
        Node* temp = head;
        head = head->next;
        free(temp);
        return head;
    }
    for (int i = 0; i < position; i++)
    {
        current = current->next;
    }
    if (current->next == NULL) return head;
    Node* temp = current->next;
    current->next = current->next->next;
    free(temp);
    return head;
}
int search(Node* head,int target){
    if (head==NULL) return -1;
    Node* current = head;
    int position = 0;
    while (current!= NULL){
        if (current->data == target){
            return position;
        }
        current = current->next;
        position++;
    }
    return -1;
}
Node* deleteBegining(Node* head){
    if (head == NULL) {
        printf("Linked lis empty");
        return head;
    }
    Node* temp = head;
    head = head->next;
    printf("Deleted Node");
    free(temp);
    return head;
}
Node* deleteAtEnd(Node* head){
    if (head == NULL)
    {
        printf("LinkedList empty");
        return head;
    }
    if (head->next == NULL){
        printf("Deleted node at end");
        free(head);
        return NULL;
    }
    Node* temp = head;
    while(temp->next->next!=NULL){
        temp = temp -> next;
    }
    Node* toDelete = temp;
    temp ->next = NULL;
    printf("Deleted data");
    free(toDelete);
    return head;
}
void display(Node*head){
    
    if (head==NULL){
        printf("lINKED List empty!");
        return;
    }
    printf("Linked List: ");
    Node* current = head;
    while(current != NULL){
        printf("%d",current->data);
        if(current->next != NULL){
            printf(" -> ");
        }
        current = current->next;
    }
    printf("->NULL\n");
}

// int secondlastNodeData(Node* head){
//     if (head==NULL || head->next != NULL){
//         return 0;
//     }
//     Node* current = head;

//     while (current->next->next != NULL){
//         current = current->next;
//     }
//     return current->data;
    
// }
void freeList(Node* head){
    Node* current = head;
    Node* next;
    while(current != NULL){
        next = current->next;
        free(current);
        current= next;
    }
}

Node* reverse(Node* head){
    Node* prev = NULL;
    Node* current = head;
    Node* next = NULL;
    while(current != NULL){
        next = current->next;
        current-> next = prev;
        prev= current;
        current =next;
    }
    return prev;
}
int main(){
    Node* head = NULL;
    printf("=== Linked List Operations Demo ===\n\n");
    printf("Inserting elements...\n");
    head = insertAtBeginning(head, 10);
    head = insertAtBeginning(head, 20);
    head = insertAtEnd(head, 5);
    head = insertAtPosition(head, 15, 2);
    
    printf("List after insertions: ");
    display(head);
    printf("Length: %d\n\n", countNodes(head));
    
    // Search operation
    int searchValue = 15;
    int position = search(head, searchValue);
    if (position != -1) {
        printf("Value %d found at position %d\n", searchValue, position);
    } else {
        printf("Value %d not found\n", searchValue);
    }
    
    // Delete operations
    printf("\nDeleting value 20...\n");
    head = deleteByValue(head, 20);
    printf("List after deletion: ");
    display(head);
    
    printf("\nDeleting at position 1...\n");
    head = deleteAtPosition(head, 1);
    printf("List after deletion: ");
    display(head);
    
printf("\nReversing the list...\n");
    head = reverse(head);
    printf("Reversed list: ");
    display(head);
    
    // Clean up
    freeList(head);


    printf("=== Linked List Deletion Demo ===\n\n");
    
    // Create a list: 10 -> 20 -> 30 -> 40 -> 50
    head = insertAtEnd(head, 10);
    head = insertAtEnd(head, 20);
    head = insertAtEnd(head, 30);
    head = insertAtEnd(head, 40);
    head = insertAtEnd(head, 50);
    
    printf("Initial list:\n");
    display(head);
    
    // Delete at beginning
    printf("\n--- Delete at Beginning ---\n");
    head = deleteAtBeginning(head);
    display(head);
    
    head = deleteAtBeginning(head);
    display(head);
    
    // Delete at end
    printf("\n--- Delete at End ---\n");
    head = deleteAtEnd(head);
    display(head);
    
    head = deleteAtEnd(head);
    display(head);
    
    head = deleteAtEnd(head);
    display(head);
    
    // Try deleting from empty list
    printf("\n--- Try deleting from empty list ---\n");
    head = deleteAtBeginning(head);
    head = deleteAtEnd(head);
    
    // Test with single node
    printf("\n--- Test with single node ---\n");
    head = insertAtBeginning(head, 100);
    printf("Single node list:\n");
    display(head);
    
    printf("Delete at beginning:\n");
    head = deleteAtBeginning(head);
    display(head);
    
    head = insertAtBeginning(head, 200);
    printf("Single node list:\n");
    display(head);
    
    printf("Delete at end:\n");
    head = deleteAtEnd(head);
    display(head);
    
    return 0;
}
*/
#include <stdio.h>
#include <stdlib.h>

// Node structure
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    (*newNode).data = data;
    (*newNode).next = NULL;
    return newNode;
}

// Insert at the beginning (helper function)
Node* insertAtBeginning(Node* head, int data) {
    Node* newNode = createNode(data);
    (*newNode).next = head;
    return newNode;
}

// Insert at the end (helper function)
Node* insertAtEnd(Node* head, int data) {
    Node* newNode = createNode(data);
    
    if (head == NULL) {
        return newNode;
    }
    
    Node* current = head;
    while ((*current).next != NULL) {
        current = (*current).next;
    }
    (*current).next = newNode;
    return head;
}
// Insert at a specific position (0-indexed)
Node* insertAtPosition(Node* head, int data, int position) {
    if (position < 0) {
        printf("Position cannot be negative\n");
        return head;
    }
    
    if (position == 0) {
        return insertAtBeginning(head, data);
    }
    
    Node* newNode = createNode(data);
    Node* temp = head;
    
    for (int i = 0; i < position - 1 && temp != NULL; i++) {
        temp = temp->next;
    }
    
    if (temp == NULL) {
        printf("Position out of bounds\n");
        free(newNode);
        return head;
    }
    
    newNode->next = temp->next;
    temp->next = newNode;
    return head;
}
// 1. Delete at the beginning
Node* deleteAtBeginning(Node* head) {
    // Check if list is empty
    if (head == NULL) {
        printf("List is empty, cannot delete\n");
        return NULL;
    }
    
    // Store the node to be deleted
    Node* nodeToDelete = head;
    
    // Move head to the next node
    head = (*head).next;
    
    // Free the memory of deleted node
    printf("Deleted node with data: %d\n", (*nodeToDelete).data);
    free(nodeToDelete);
    
    return head;
}

// 2. Delete at the end
Node* deleteAtEnd(Node* head) {
    // Check if list is empty
    if (head == NULL) {
        printf("List is empty, cannot delete\n");
        return NULL;
    }
    
    // If there's only one node
    if ((*head).next == NULL) {
        printf("Deleted node with data: %d\n", (*head).data);
        free(head);
        return NULL;
    }
    
    // Traverse to find the second last node
    Node* current = head;
    while ((*(*current).next).next != NULL) {
        current = (*current).next;
    }
    
    // Store the last node to be deleted
    Node* nodeToDelete = (*current).next;
    
    // Remove the connection to last node
    (*current).next = NULL;
    
    // Free the memory of deleted node
    printf("Deleted node with data: %d\n", (*nodeToDelete).data);
    free(nodeToDelete);
    
    return head;
}
// Delete at a specific position (0-indexed)
Node* deleteAtPosition(Node* head, int position) {
    if (head == NULL || position < 0) {
        return head;
    }
    
    // Delete head
    if (position == 0) {
        Node* temp = head;
        head = head->next;
        free(temp);
        return head;
    }
    
    Node* current = head;
    for (int i = 0; i < position - 1 && current->next != NULL; i++) {
        current = current->next;
    }
    
    if (current->next == NULL) {
        return head;
    }
    
    Node* temp = current->next;
    current->next = current->next->next;
    free(temp);
    return head;
}
// Display the linked list
void display(Node* head) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    
    printf("List: ");
    Node* current = head;
    while (current != NULL) {
        printf("%d", (*current).data);
        if ((*current).next != NULL) {
            printf(" -> ");
        }
        current = (*current).next;
    }
    printf(" -> NULL\n");
}
// Search for a value
int search(Node* head, int value) {
    Node* current = head;
    int position = 0;
    
    while (current != NULL) {
        if (current->data == value) {
            return position;
        }
        current = current->next;
        position++;
    }
    return -1; // Not found
}

// Get length of the list
int getLength(Node* head) {
    int length = 0;
    Node* current = head;
    
    while (current != NULL) {
        length++;
        current = current->next;
    }
    return length;
}
// Free the entire list
void freeList(Node* head) {
    Node* current = head;
    Node* next;
    
    while (current != NULL) {
        next = (*current).next;
        free(current);
        current = next;
    }
}

// Example usage
int main() {
    Node* head = NULL;
    
    printf("=== Linked List Operations Demo ===\n\n");
    
    // Create initial list
    head = insertAtBeginning(head, 10);
    head = insertAtBeginning(head, 20);
    head = insertAtEnd(head, 5);
    head = insertAtPosition(head, 15, 2);
    
    printf("Initial list:\n");
    display(head);
    printf("Length: %d\n\n", getLength(head));
    
    // Delete at beginning
    printf("--- Delete at Beginning ---\n");
    head = deleteAtBeginning(head);
    display(head);
    
    // Delete at end
    printf("\n--- Delete at End ---\n");
    head = deleteAtEnd(head);
    display(head);
    
    // Delete at specific position
    printf("\n--- Delete at Position 1 ---\n");
    head = deleteAtPosition(head, 1);
    display(head);
    
    // Try deleting from empty list after clearing all
    head = deleteAtBeginning(head);
    display(head);
    
    printf("\n--- Try deleting from empty list ---\n");
    head = deleteAtBeginning(head);
    head = deleteAtEnd(head);
    
    // Test with single node
    printf("\n--- Test with single node ---\n");
    head = insertAtBeginning(head, 100);
    printf("Single node list:\n");
    display(head);
    
    printf("Delete at beginning:\n");
    head = deleteAtBeginning(head);
    display(head);
    
    return 0;
}