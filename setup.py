from setuptools import setup, find_packages

setup(
    name='jointiles',
    version='0.1',
    description='Tool to full outer join two tiles spatially',
    author='Jorge Anais',
    url='https://github.com/jorgeanais/jointiles',
    author_email='jrganais@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'astropy', 'scipy', 'ipython', 'yaml', 'PyYAML'],
    package_data={
        '': ['*.md'],
    },
    zip_safe=False,
)