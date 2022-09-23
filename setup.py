from setuptools import setup

setup(
    name='charle_s_lib',
    version='0.0.1',
    description='My own library for data analysis',
    py_modules=["charles_lib"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python ::3",
        "Programming Language :: Python ::3.6",
    ],
    install_requires=[
        "blessings ~= 1.7",
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
    author="Charles Dupret",
    author_email="charles.dupret@grenoble-inp.org",
)