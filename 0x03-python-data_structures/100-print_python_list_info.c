#include <Python.h>

/**
 * print_python_list_info - Display detailed attributes of a Python list object.
 * @p: Pointer to a PyObject list.
 * Description: prints the size of the list, the space currently allocated
 * to the list, and the type of each element within the list.
 */
void print_python_list_info(PyObject *p)
{
	int list_len, space_allocated, idx;
	PyObject *list_item;

	list_len = Py_SIZE(p);
	space_allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", space_allocated);

	for (idx = 0; idx < list_len; idx++)
	{
		list_item = PyList_GetItem(p, idx);
		printf("Element %d: %s\n", idx, Py_TYPE(list_item)->tp_name);
	}
}
