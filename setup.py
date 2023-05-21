from distutils.core import setup, Extension


def main():
    setup(
        name="generator",
        version="1.0.0",
        description="what's description?",
        ext_modules=[Extension("generator", ["generator.c"])],  # extra_compile_args=["-O2"]
    )


if __name__ == "__main__":
    main()