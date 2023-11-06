#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - print python list
 * @p: pointer to python list object
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;

	PyListObject *obj = (PYListObject *);
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0 ; i < l ; i++)
		printf("Element %i: %S\n", Py_TYPE(obj->ob_item[i])->tp_name);
}
