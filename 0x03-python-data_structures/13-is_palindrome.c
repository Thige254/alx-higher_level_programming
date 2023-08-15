/*
 * File: 13-is_palindrome_refactored.c
 * Auth: Thige Jay
 */

#include "lists.h"

listint_t *reverse_list(listint_t **head);
int is_list_palindrome(listint_t **head);

/**
 * reverse_list - Reverses a singly-linked list.
 * @head: A pointer to the address of the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next_node = NULL;

	while (current)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}

	*head = prev;
	return (*head);
}

/**
 * is_list_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the address of the head of the linked list.
 *
 * Return: 0 if the linked list is not a palindrome.
 *         1 if the linked list is a palindrome.
 */
int is_list_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = *head;

	if (!*head || !(*head)->next)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast)
		slow = slow->next;

	second_half = slow;
	prev_slow->next = NULL;
	reverse_list(&second_half);

	while (*head && second_half)
	{
		if ((*head)->n != second_half->n)
		{
			reverse_list(&second_half);
			return (0);
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}

	reverse_list(&second_half);
	return (1);
}
