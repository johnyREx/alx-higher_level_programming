#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints basic information about Python bytes objects
 * @p: pointer to Python objects
 *
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t len = 0, size = 0, i = 0;

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		printf("  size: %lu\n", PyBytes_Size(p));

		str = PyBytes_AsString(p);
		printf("  trying string: %s\n", str);

		len = size < 10 ? size + 1 : 10;
		printf("  first %ld bytes:", len);
		for (i = 0; i < len; i++)
			printf(" %02x", (unsigned char)str[i]);
		printf("%s", "\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}




/**
 * print_python_list - prints basic info about python lists
 * @p: pointer to a python PyObject
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t p_len, i = 0;
	PyObject *elem;
	PyObject *type;

	p_len = ((PyVarObject *)p)->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", p_len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < p_len; i++)
	{
		elem = ((PyListObject *)p)->ob_item[i];
		if (elem)
		{
			type = PyObject_Type(elem);
			printf("Element %ld: %s\n", i, ((PyTypeObject *)type)->tp_name);
			if (PyBytes_Check(elem))
				print_python_bytes(elem);
			Py_DECREF(type);
		}
	}
}
