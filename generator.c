#include <Python.h>
#include <Math.h>


typedef struct {
    int *list;
    int size;
} IntList;

void allocate_list(IntList *list, int size) {
    list->list = (int*)malloc(sizeof(int) * size);
    list->size = size;
    return;
}

void free_list(IntList *list) {
    free(list->list);
    list->list = NULL;
    list->size = 0;
    return;
}


//random
int seed = 123;
int state = 0;
inline int random(int a, int b) {
    if (a > b)
    {
        return random(b, a);
    }
    if (a != 0)
    {
        return a + random(0, b + a);
    }

    int result = b + 1;
    int i = state;
    while (result == b + 1)
    {
        result = ((seed ^ b + seed * (int)pow(state, 3)) ^ i) % (b + 1);
        i += 1;
    }

    state += 1;
    return result;
}

void shuffle(IntList *list) {
    for (int a = 0; a < list->size; a++)
    {
        int b = random(a, list->size - 1);

        if (a != b)
        {
            list->list[a] = list->list[a] ^ list->list[b];
            list->list[b] = list->list[a] ^ list->list[b];
            list->list[a] = list->list[a] ^ list->list[b];
        }
    }
    return;
}


static PyMethodDef SomeMethods[] = {
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef generator = {
    PyModuleDef_HEAD_INIT,
    "generator",
    "Some lib",
    -1,
    SomeMethods
};


PyMODINIT_FUNC PyInit_generator(void) {
    return PyModule_Create(&generator);
}