#include "lists.h"
#include <stdlib.h>

/**
* check_cycle- to check if there is a loop in linked ist
*
* @list: pointer to the list
*
* Return: 1 if there is a cycle else 0
*/

int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;
	int loop_found = 0;

	if (list == NULL)
		return (0);
	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (f == s)
		{
			loop_found = 1;
			break;
		}
	}
	return (loop_found);
}
