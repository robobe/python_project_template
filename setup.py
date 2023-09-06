from setuptools import setup, find_packages
from #{project_name} import __version__

setup(
    name='#{project_name}',
    version=__version__,
    author='#{author}',
    author_email='#{author_email}',
    description='#{project_description}',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "#{project_name}=#{project_name}.app:main"
        ]
    }
)
