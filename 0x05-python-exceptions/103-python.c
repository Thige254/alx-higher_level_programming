#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * Print basic information about a Python list.
 * @param p: Pointer to a Python list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, index;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Not a valid list object\n");
		return;
	}

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the list = %zd\n", size);
	printf("[*] Memory allocated for list = %zd\n", alloc);

	for (index = 0; index < size; index++)
	{
		item = PyList_GetItem(p, index);
		printf("Element %zd: %s\n", index, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * Print basic information about Python bytes.
 * @param p: Pointer to a Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, index;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Not a valid bytes object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %zd\n", size);
	printf("  decoded string: %s\n", str);
	if (size > 10)
		size = 10;
	printf("  first %zd bytes: ", size + 1);
	for (index = 0; index <= size && index < 10; index++)
	{
		printf("%02hhx", str[index]);
		if (index < 9 && index != size)
			printf(" ");
	}
	printf("\n");
}

/**
 * Print basic information about a Python float.
 * @param p: Pointer to a Python float object.
 */
void print_python_float(PyObject *p)
{
	double val;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Not a valid float object\n");
		return;
	}

	val = PyFloat_AS_DOUBLE(p);
	printf("  value: %lf\n", val);
}
