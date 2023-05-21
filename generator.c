#include <Python.h>
#include <Math.h>

//random
int seed = 123;
int state = 0;
inline int random(int a, int b)
{
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
        result = ((seed + seed * (int)pow(state, 3)) ^ i) % (b + 1);
        i += 1;
    }

    state += 1;
    return result;
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