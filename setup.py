from setuptools import find_packages, setup

setup(
    name='music_app',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
