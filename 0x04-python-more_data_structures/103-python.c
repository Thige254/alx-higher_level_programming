#include <stdio.h>
#include <Python.h>

/**
 * display_bytes_info - Show information about Python bytes
 *
 * @py_obj: Python Object
 * Return: Nothing
 */
void display_bytes_info(PyObject *py_obj)
{
    char *byte_str;
    long int byte_length, idx, display_limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(py_obj))
    {
        printf("  [ERROR] Not a Bytes Object\n");
        return;
    }

    byte_length = ((PyVarObject *)(py_obj))->ob_size;
    byte_str = ((PyBytesObject *)py_obj)->ob_sval;

    printf("  size: %ld\n", byte_length);
    printf("  trying string: %s\n", byte_str);

    display_limit = (byte_length >= 10) ? 10 : byte_length + 1;
    printf("  first %ld bytes:", display_limit);

    for (idx = 0; idx < display_limit; idx++)
    {
        if (byte_str[idx] >= 0)
            printf(" %02x", byte_str[idx]);
        else
            printf(" %02x", 256 + byte_str[idx]);
    }

    printf("\n");
}

/**
 * display_list_info - Show information about Python list
 *
 * @py_obj: Python Object
 * Return: Nothing
 */
void display_list_info(PyObject *py_obj)
{
    long int list_size, idx;
    PyListObject *py_list;
    PyObject *item;

    list_size = ((PyVarObject *)(py_obj))->ob_size;
    py_list = (PyListObject *)py_obj;

    printf("[*] Python list info\n");
    printf("[*] Total items in the Python List = %ld\n", list_size);
    printf("[*] Allocated = %ld\n", py_list->allocated);

    for (idx = 0; idx < list_size; idx++)
    {
        item = ((PyListObject *)py_obj)->ob_item[idx];
        printf("Element %ld: %s\n", idx, ((item)->ob_type)->tp_name);
        if (PyBytes_Check(item))
            display_bytes_info(item);
    }
}
