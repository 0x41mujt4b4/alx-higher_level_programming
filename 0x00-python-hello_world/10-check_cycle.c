#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check if list has a cycle
 *
 * @list: the list to be checked
 *
 * Return: 0 if there is no cycle 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;
	while (current != NULL)
	{
		if (current->visited == 1)
			return (1);
		current->visited = 1;
		current = current->next;
	}
	return (0);
}
