#include <Python.h>

/**
 * print_python_list_info - Prints detailed information about a Python list.
 * @py_list: A pointer to a Python list object.
 *
 * Description: retrieves and displays the size and memory allocation
 * details of a Python list.
 * prints the type of each element.
 */
void print_python_list_info(PyObject *py_list)
{
	int list_size, memory_allocated, index;
	PyObject *element;

	list_size = Py_SIZE(py_list);
	memory_allocated = ((PyListObject *)py_list)->allocated;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Memory Allocated (in elements) = %d\n", memory_allocated);

	for (index = 0; index < list_size; index++)
	{
		printf("Element %d: ", index);

		element = PyList_GetItem(py_list, index);
		printf("%s\n", Py_TYPE(element)->tp_name);
	}
}
