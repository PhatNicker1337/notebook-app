from setuptools import setup, find_packages

setup(
    name="notebook-app",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'notebook=notebook.cli:main',
        ],
    },
    author="PhatNicker1337",
    description="Простое консольное приложение для заметок",
)