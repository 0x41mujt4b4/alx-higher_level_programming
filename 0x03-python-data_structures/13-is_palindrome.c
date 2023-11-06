#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if linked list palindrome
 * @head: the linked list to be checked
 *
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	unsigned int n, i, j;
	int *arr;

	current = *head;
	if (current == NULL)
		return (1);
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	arr = malloc(n * sizeof(int));
	if (arr == NULL)
		return (0);
	current = *head;
	for (i = 0; i < n; i++)
	{
		arr[i] = current->n;
		current = current->next;
	}
	for (i = 0, j = n - 1; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
