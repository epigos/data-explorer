import os
from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.md'),
          'r') as f:
    readme_content = f.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt'),
          'r') as f:
    install_requires = f.read()


setup(
    name="dexplorer",
    version='0.1.1',
    description="View, summarize and visualize data in the browser",
    author="Philip Adzanoukpe",
    author_email="epigos@gmail.com",
    url="https://github.com/epigos/data-explorer",
    license="MIT License",
    long_description=readme_content,
    packages=find_packages(),
    package_data={'dexplorer': ['static/*/*', 'templates/*',
                                'requirements.txt', 'README.md']},
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
