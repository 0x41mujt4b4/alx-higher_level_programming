#include <stdio.h>
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
	unsigned int n;

	current = *head;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	current = *head;
	int arr[n];
	int i = 0;
	int j = n - 1;

	while (current != NULL)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	i = 0;
	while (i < j)
	{
		if (arr[i] != arr[j])
			return (0);
		i++;
		j--;
	}
	return (1);
}
