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
	listint_t *new;
	listint_t *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	temp = *head;
	if (temp == NULL)
		temp = new;
	while (temp != NULL)
	{
		if (temp->n == 4)
		{
			new->next = temp->next;
			temp->next = new;
		}
		temp = temp->next;
	}
	return (new);
}
