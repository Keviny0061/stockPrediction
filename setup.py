from setuptools import setup, find_packages

setup(
    name="stock_analysis_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'stock_analysis_app = main:main',
        ],
    },
)
