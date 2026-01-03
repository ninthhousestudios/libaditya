# README

```libaditya``` is an astrological calculation library meant to be easily understood in terms
of what calculations are performed and how they are done. it includes a sample program
called ```pyphemeris```.

```pyphemeris``` ideally is meant to serve as an easily readable documentation on how
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

## Usage

if pyhd is called with no arguments
```sh
pyhd
```

it will produce a bodygraph for the time the program runs, which will be placed
in ``` pyhd_constants.bodygraphs_path ``` with the format

```year-month-day-hour-minute-second-bodygraph.svg```

note: all times are UTC

### Input

Information can be passed in the following ways:

#### Manually

```sh
-d/--date MM/DD/YYYY
-t/--time HH:MM:SS 
-n/--name name 
```

Time must be 24-hour UTC format

``` -n/--name ``` parameter is optional

if one or both of date or time is not specificed, the current date or time at
runtime will be used

#### .chtk file

a Kala chart file can be passed in this way:

```sh
pyhd -i file.chtk
```

if the .chtk is in the directory ```pyhd_path/charts/```, then the file extension is
not necessary

```sh
pyhd -i file
```

#### .pyhd file

a .pyhd file has the following format

```
Name = (optional)
Date = MM/DD/YYYY
Time = HH:MM:SS
```

Time must be 24-hour UTC time. There is a template in the
```pyhd_path/charts/``` folder, ``` template.pyhd ```. If you .pyhd file is in
```charts/```, then the file extension is not necessary. ```chtk2pyhd``` can take a
.chtk file and write a .pyhd file.

### Output

The ```-o/--output``` flag can be used to manually specifly the output file
name.

This parameter is optional.

If not included, the bodygraph will be written to the folder
```pyhd_path/bodygraphs/ (=pyhd_constants.bodygraphs_path)``` with the
format 

```(input-file-root)-bodygraph.svg```

### Transits

```pyhd``` can draw transit charts as well.

```pyhd -T```

will draw a chart that includes only the transit gates for the moment the
program is run.

```-D/--transit-date``` and ```-H/--transite-time``` specify transit date and time respectively.

If any bodygraph information is given, by ```-d/-t``` or by ```-i```, then ```pyhd``` will
draw the transit chart for that bodygraph.

### Composite

```pyhd``` can draw two-person composite charts.

Information for the first person is passed with the ```-i/--input``` flag and
appears on the right in the "conscious" color (as defined in the theme).

Information for the second person is passed with the ```-c/--composite``` flag
and apppears on the left in the "unconscious" color (as defined in the theme).

### Dreamgraph

```pyhd``` can draw dreamgraphs chart, the supposed design we have while
sleeping.

Use the ```-s/--dream``` flag for this option.

## Configuration

Configuration is done with a theme file.

Themes can be located in the ```pyhd_path/themes/``` folder.
Theme can be passed with the ```-m/--theme``` flag. If the theme is in the
```themes/``` folder, the file name can be passed by itself.

Default theme can be set with the ```default_theme``` variable in
```pyhd_constants.py```

The theme contains color information. Most of the parameters are commented to
explain their function.

## Options

```sh

usage: pyhd [options]

draw a human design bodygraph

options:
  -h, --help            show this help message and exit
  -i, --input INPUT     input file with birth data; can be a .chtk or .pyhd file; if file is in $pyhdpath/charts/ directory, dont need to
                        include file extension
  -d, --date DATE       date specified as MM/DD/YYYY; if not present will use day at runtime if an input file is not specified
  -t, --time TIME       time specified as HH:MM:SS, (utc); if not present will use time at runtime if an input file is not specified
  -n, --name NAME       name of person for the bodygraph (optional)
  -g, --gates GATES     choose the why gates are displayed: options are: numbers, hexagrams
  -T, --transit         create a transit chart; by itself or in combination with -D and/or -H will create a chart of only the transits are the
                        specified time; with -i or -d/-t options will create a bodygraph with transit added
  -D, --transit-date TRANSIT_DATE
                        date for the transit, MM/DD/YYYY; not specified, will use date at runtime
  -H, --transit-time TRANSIT_TIME
                        time for the transit, HH:MM:SS, 24-hour UTC format; not specified, will use time at runtime
  -c, --composite COMPOSITE
                        draw a composite bodygraph; the person on the left will specified by the file passed to -i/--input; the person on the
                        right to -c/--composite
  -s, --dream           draw a dreamgraph
  -m, --theme THEME     theme file to use. default directory is $pydhpath/themes
  -p, --print-planet-info
                        print planet information to stdout
  -o, --output-file OUTPUT_FILE
                        (optional) name of output file; use extenstion .svg or .png to indicate which format to use
  -X, --xx              use 193.25 ecliptic longitude for gate 1; default output file name will include 'X' just before extension
```
