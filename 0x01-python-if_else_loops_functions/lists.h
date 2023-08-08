#include <stdlib.h>

typedef struct listint_t {
	int n;
	struct listint_t *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
