#include "lists.h"
#include <stdlib.h>

/**
* size_list- to get the number of nodes on a list
*
* @h: pointer to the head
*
* Return: Number of nodes
*/

int size_list(listint_t *h)
{
	int n = 0;

	while (h != NULL)
	{
		n++;
		h = h->next;
	}
	return (n);
}
/**
* reverse_list - reverses the linked list
*
* @temp: pointer to tempoarary node
*
* Return: the head of the node
*/

listint_t *reverse_list(listint_t *temp)
{
	listint_t *prev = NULL, *next = NULL;
	listint_t *current = temp;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
/**
* is_palindrome- to check if list is palindrome
*
* @head: pointer to a pointer to head
*
* Return: 1 if palindrom else 0
*/

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *reversed;
	int mid, n = 1, size, pali_found = 1;

	if (*head == NULL)
		return (1);
	size = size_list(*head);
	if (size % 2 == 0)
		mid = size / 2;
	else
		mid = (size + 1) / 2;
	while (*head != NULL)
	{
		if (n == mid)
		{
			reversed = reverse_list((*head)->next);
			while ((current != NULL) && (reversed != NULL))
			{
				if ((current->n) != (reversed->n))
				{
					pali_found = 0;
					break;
				}
				current = current->next;
				reversed = reversed->next;
			}
		}
		n++;
		*head = (*head)->next;
	}
	return (pali_found);
}
