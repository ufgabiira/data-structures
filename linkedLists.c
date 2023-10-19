#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} node;

typedef struct {
    int len;
    node *head;
} list;

list create_list();
void insert_node(list *l, int val);
int get_value(list *l, int index);

int main(void) {

    list linked_list = create_list(); 

    for(int i = 0; i < 10; i++) {
        int input;
        printf("Elemento %d = ", i);
        scanf("%d%*c", &input);
        insert_node(&linked_list, input); 
    }

    printf("\n\n----- Resultado -----\n");

    for(int i = 0; i < linked_list.len; i++) {
        printf("Elemento %d -> %d\n", i, get_value(&linked_list, i));
    }

    return 0;
}

// Cria a lista
list create_list() {

    node *head = malloc(sizeof(node));
    head->next = NULL;

    list l;
    l.len = 0;
    l.head = head;

    return l;
}

// Adiciona novos valores à lista
void insert_node(list *l, int val) {

    node *tmp = l->head;

    while(tmp->next) {
        tmp = tmp->next;
    }

    node *new_node = malloc(sizeof(node));
    new_node->data = val;
    new_node->next = NULL;
    tmp->next = new_node;
    l->len++;

}

// Retorna o valor guardado no nó indicado
int get_value(list *l, int index) {

    node *tmp = l->head;

    for(int i = -1; i < index; i++) {
        tmp = tmp->next;
    }

    return tmp->data;
}