#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: pointer to pointer of first node
 * Return: 1 if is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0;
	listint_t *iter, *fast_ptr, *slow_ptr, *prev, *current;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	iter = *head;
	fast_ptr = *head;
	slow_ptr = *head;
	prev = *head;
	while (fast_ptr && fast_ptr->next)
	{
		len++;
		prev = slow_ptr;
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}
	while (iter != prev)
	{
		current = iter->next;
		iter->next = prev->next;
		prev->next = iter;
		iter = current;
	}
	*head = iter;
	if (fast_ptr)
		slow_ptr = slow_ptr->next;
	for (i = 0; i < len; i++)
	{
		if (iter->n != slow_ptr->n)
			return (0);
		iter = iter->next;
		slow_ptr = slow_ptr->next;
	}
	return (1);
}
