#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - Prints info about python list
 * @p: Python List Object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int allocated, size, i;
	PyListObject *list = (PyListObject *)p;
	PyObject *list_item;

	size = Py_SIZE(list);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		list_item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(list_item)->tp_name);
	}
}
