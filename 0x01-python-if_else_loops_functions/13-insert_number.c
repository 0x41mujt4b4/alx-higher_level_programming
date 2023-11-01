#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node into list
 * @head: the list
 * @number: the value to add
 *
 * Return: address of inserted node or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
		*head = new;
	else if (new->n <= current->n)
	{
		new->next = current;
		current = new;
	}
	else
	{
		while (current != NULL && current->next->n < new->n)
			current = current->next;
		if (current == NULL)
			current->next = new;
		else
		{
			new->next = current->next;
			current->next = new;
		}
	}
	return (new);
}
