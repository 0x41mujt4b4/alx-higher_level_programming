#include "Python.h"
#include <stdio.h>
/**
 * print_python_list_info - print python list
 * @p: pointer to python list object
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int i, l;

	l = PyList_Size(p)
	for (i = 0 ; i < l ; i++)
		printf("[*] Size of the Python List = %d", l);
}
