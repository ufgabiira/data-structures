#include <stdio.h>
#include <stdlib.h>

typedef struct _node {
    int data;
    struct _node *previous;
} node;

typedef struct _stack{
    unsigned int len;
    node *head;
} stack;

stack create_stack();
void push(stack *s, int value);
node* pop(stack *s);
void clean_stack(stack *s);

// Play with it
int main(void) { 

    stack s = create_stack();

    push(&s, 10);
    push(&s, 5);
    push(&s, 549);

    free(pop(&s));

    clean_stack(&s);
}

// create a stack
stack create_stack() {

    // create and initialize new stack
    stack s;
    s.len = 0;

    // return new stack
    return s;
}

// add new elements (nodes) to the top of the stack
void push(stack *s, int value) {

    // create a new node
    node *new_node = malloc(sizeof(node));

    // insert the value to the new node
    new_node->data = value;

    // make the new node point to the stack's top node
    new_node->previous = s->head;

    // the new node becomes the stack head
    s->head = new_node;

    // increase the stack length member
    s->len++;
}

// Remove the last added element (node)
//? Should this function return the removed node or delete it?
//? Feels like would be better to delete, but what if the user
//? want to do something with it?
node* pop(stack *s) {

    // `removed` is the stack head (last added node)
    node *removed = s->head;

    // node before `removed` is now the stack head
    s->head = removed->previous;

    // free(top_node);
    return removed;
}

// Delete all the stack nodes
//? Is this really needed?
//? I think its easier to just use free() in the main function directly
//? and this kind of abstraction may be dumb, but having it kinda feels nice
void clean_stack(stack *s) {

    if (s->len == 1) {
        free(s->head);
    } else {
        while(s->head->previous != NULL) {
            free(pop(s));
            s->len--;
        } 
        free(pop(s));
    }   
}