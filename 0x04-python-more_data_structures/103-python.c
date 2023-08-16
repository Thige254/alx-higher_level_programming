#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Show information about Python bytes
 *
 * @py_obj: Python Object
 * Return: Nothing
 */
void print_python_bytes(PyObject *py_obj)
{
    char *byte_data;
    long int data_len, idx, display_limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(py_obj))
    {
        printf("  [ERROR] Not a Bytes Object\n");
        return;
    }

    data_len = ((PyVarObject *)(py_obj))->ob_size;
    byte_data = ((PyBytesObject *)py_obj)->ob_sval;

    printf("  size: %ld\n", data_len);
    printf("  trying string: %s\n", byte_data);

    display_limit = (data_len >= 10) ? 10 : data_len + 1;
    printf("  first %ld bytes:", display_limit);

    for (idx = 0; idx < display_limit; idx++)
    {
        if (byte_data[idx] >= 0)
            printf(" %02x", byte_data[idx]);
        else
            printf(" %02x", 256 + byte_data[idx]);
    }

    printf("\n");
}

/**
 * print_python_list - Show information about Python list
 *
 * @py_obj: Python Object
 * Return: Nothing
 */
void print_python_list(PyObject *py_obj)
{
    long int list_len, idx;
    PyListObject *list_obj;
    PyObject *list_item;

    list_len = ((PyVarObject *)(py_obj))->ob_size;
    list_obj = (PyListObject *)py_obj;

    printf("[*] Python list info\n");
    printf("[*] Total items in the Python List = %ld\n", list_len);
    printf("[*] Allocated = %ld\n", list_obj->allocated);

    for (idx = 0; idx < list_len; idx++)
    {
        list_item = ((PyListObject *)py_obj)->ob_item[idx];
        printf("Element %ld: %s\n", idx, ((list_item)->ob_type)->tp_name);
        if (PyBytes_Check(list_item))
            print_python_bytes(list_item);
    }
}
