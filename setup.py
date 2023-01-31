
from setuptools import setup, find_packages
import codecs
import os


# with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()

VERSION = '0.0.6'
DESCRIPTION = 'It a convertor that you use ! likely'
LONG_DESCRIPTION = 'A package that convert a line to interger_calculator '
det = '''

![python function](https://miro.medium.com/max/1400/1*WWrXceae4H_klzpPU6h7Hg.png)
**Why you should choose that , let's check**

> Simple and powerfull ,
> Best for discord bot reply Best for where string,
> simple function with high return


## **How to import**

```
import muradian
from muradian import msc
```



## Fixed number calculation
```
msc.stca('digit firstNum operator lastNum

genarally use: stca('1 2 pl 3')
here,
1 is digit (how many digit you want to use)
2 and 3 is digit that will summation by 'pl' command

		print('2 23 mi 21') 
pl = Pluse / Summation
mi = Substraction
mu = Multiplication
di = Division
```

## 1 to N number
*how to pass string to for sum , example :*
```
print(mustca.msum('1 2 3 4')
```
```
	output: 10
```
how to pass string to for avg , example :*
```
print(mustca.msum('2 2 2')
```
```
	output: 2
```

## contact:
[Github](https://github.com/mozaddedalfeshani) </br>
[messenger](m.me/mozaddedalfeshani)


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
