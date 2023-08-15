#include <Python.h>

/**
 * display_python_list_info - Show details about Python lists.
 * @py_list: A pointer to a Python list object.
 */
void display_python_list_info(PyObject *py_list)
{
	Py_ssize_t size, index;
	Py_ssize_t allocated;
	PyObject *item;

	size = PyList_Size(py_list);
	allocated = ((PyListObject *)py_list)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (index = 0; index < size; index++)
	{
		item = PyList_GetItem(py_list, index);
		printf("Element %zd: %s\n", index, Py_TYPE(item)->tp_name);
	}
}
