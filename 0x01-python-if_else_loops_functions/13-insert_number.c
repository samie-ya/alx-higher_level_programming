#include "lists.h"
#include <stdlib.h>

/**
* insert_node- to insert a node in linked list
*
* @head: pointer to pointer to head
*
* @number: the number to be inserted
*
* Return: the address of the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *next;
	listint_t *h = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if ((*head)->n > new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (h != NULL)
	{
		next = h->next;
		if (next != NULL)
		{
			if (next->n > new->n)
			{
				h->next = new;
				new->next = next;
				return (new);
			}
		}
		else
		{
			h->next = new;
			new->next = NULL;
			return (new);
		}
		h = h->next;
	}
	return (NULL);
}
