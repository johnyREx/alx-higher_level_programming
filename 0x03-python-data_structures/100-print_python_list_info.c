#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints basic info about python lists
 * @p: pointer to a python PyObject
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t p_len, i = 0;
	PyObject *elem;

	p_len = PyList_Size(p);
	printf("[*] Size of the Python List = %lu\n", p_len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < p_len; i++)
	{
		elem = PyList_GetItem(p, i);
		if (elem)
		{
			printf("Element %lu: %s\n", i, (Py_TYPE(elem)->tp_name));
		}
	}
}
