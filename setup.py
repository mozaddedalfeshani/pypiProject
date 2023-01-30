
from setuptools import setup, find_packages
import codecs
import os


# with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()

VERSION = '0.0.5'
DESCRIPTION = 'It a convertor that you use ! likely'
LONG_DESCRIPTION = 'A package that convert a line to interger_calculator '
det = '''
Why you should choose that , let's check

Simple and powerfull
Best for discord bot reply
Best for where string passing by input(a line)

*Function*
```
There have 2 function , The first one is stca and last one avg:
what's and how it work's let's check
```

```
import muradian
```

*how to pass string , example :*
```
for stca function,
Skeleton: stca('digit firstNum operator lastNum')

genarally use: stca('1 2 pl 3')

here,
1 is digit (how many digit you want to use)

2 and 3 is digit that will summation by 'pl' command

  
```
*more example :*
 ```
2 23 mi 21

pl = Pluse / Summation

mi = Substraction

mu = Multiplication

di = Division

  
```
average beetween some number, lets example:
how it's work let's check ,*Skeleton*:
```
avg('total_value digit n1 n2 n*') //return the average value of n number
```



'''


# Setting up
setup(
    name="muradian_strCalc",
    version=VERSION,
    author="Mozadded Alfeshani",
    author_email="developer.mozadded@gmail.com",
    description="A best usefull Function for assistant or text to speech services",
    long_description_content_type="text/markdown",
    long_description=det,
    packages=['muradian'],
    # package_dir={'src': 'muradian'},
    install_requires=[],
    keywords=['python', 'calcutor', 'assistant',
              'string calculator'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
