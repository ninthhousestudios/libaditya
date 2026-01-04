# README

```libaditya``` is an astrological calculation library meant to be easily understood in terms
of what calculations are performed and how they are done. it includes a sample program
called ```pyphemeris```.

```pyphemeris``` is meant to serve as an easily readable documentation on how
the library works. Each function in libaditya itself is meant to return the requested
data in a way that can then be presented in some way. Built into most ```libaditya```
classes are functions to represent themselves as text through repr (__repr__) and
```print```, i.e., through ```__str__```. ```pyphemeris``` makes use of these in order
to print the requested data to ```stdout```.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Options](#options)

## Dependencies

python, [pyswisseph](https://pypi.org/project/pyswisseph/), [python-prettytable](https://pypi.org/project/prettytable/)

written with python 3.13

## Installtion

```sh
git clone https://gitlab.com/j0sh4rp3/libaditya
```

if using ```uv``` then:
```
uv venv
source .venv/bin/activate
uv pip install -e .
```

## Usage

hopefully, ideally, then you can run
```
python pyphemeris/pyphemeris.py
```
or
```
uv run pyphemeris/pyphemeris.py
```

This will print a chart for right now at the time and place specified in
```pyphemeris/defaults.py```. You can change any of the defaults in that file, and then
most options have a flag, some of which are toggles. eventually, there will be
documentation for the options ands for what exactly each does. what it says may not be
100% accurate at the moment
