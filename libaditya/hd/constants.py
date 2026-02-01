#    This file is part of libaditya.
#
#    Copyright (c) 2025 Josh Harper <humanhaven@substack.com>
#
#    libaditya is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    libaditya is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with libaditya.  If not, see <https://www.gnu.org/licenses/>.

import swisseph as swe
import os
import pathlib

#import libaditya.constants as const
# i dont remember why this is a star import
# when if i changed it to "as const" like above, i got an import error
from libaditya.constants import *
import libaditya.constants as const

# .../libaditya/libaditya/ is the base_path
base_path = const.base_path
theme_path = base_path + "/draw/themes/"
default_theme = theme_path + "default-theme.hd"

hd_glyphs = [*glyphs.values()]

# gates of the hd i ching wheel in order
wheel=[1,43,14,34,9,5,26,11,10,58,38,54,61,60,41,19,13,49,30,55,37,63,22,36,25,17,21,51,42,3,27,24,2,23,8,20,16,35,45,12,15,52,39,53,62,56,31,33,7,4,29,59,40,64,47,6,46,18,48,57,32,50,28,44]

gate_one = 223+1/4

# sizes of gates and lines along the ecliptic
gate = 360/64
line = gate/6
color = line/6
tone = color/6
base = tone/5

# how many of each there are
how_many_gates = 64
how_many_lines = how_many_gates*6
how_many_colors = how_many_lines*6
how_many_tone = how_many_colors*6
how_many_base = how_many_tone*5

# elements of tuples in entry
# [0] = string representation of the gate number
# [1] = hexagram of gate
# [2] = x-coord for number/hexagram placement
# [3] = y-coord for number/hexagram placement
# [4] = starting x-coord for channel
# [5] = starting y-coord for channel
# [6] = end x-coord for channel
# [7] = end y-coord for channel
gates = { 1: ("01","䷀",245,230,250,230,250,208), 
         2: ("02","䷁",245,290,250,290,250,312), 
         3: ("03","䷂",245,385,250,385,250,405), 
         4: ("04","䷃",260,80,265,80,265,60),
         5: ("05","䷄",230,340,234,340,234,305),
         6: ("06","䷅",340,372,340,369,307,371),
         7: ("07","䷆",230,242,234,242,234,216),
         8: ("08","䷇",245,195,250,195,250,208),
         9: ("09","䷈",260,385,265,385,265,405),
         10: ("10","䷉",212,260,212,258,165,258),
         11: ("11","䷊",260,95,265,95,265,120),
         12: ("12","䷋",268,173,330,245,268,150),
         13: ("13","䷌",260,242,265,242,265,216),
         14: ("14","䷍",245,340,250,340,250,312),
         15: ("15","䷎",230,277,234,277,234,305),
         16: ("16","䷏",221,163,221,163,160,230),
         17: ("17","䷐",230,95,234,95,234,120),
         18: ("18","䷑",102,390,108,390,163,438),
         19: ("19","䷒",268,445,268,450,330,410),
         20: ("20","䷓",221,178,221,178,180,230),
         21: ("21","䷔",313,268,320,273,295,228),
         22: ("22","䷕",372,354,380,352,330,245),
         23: ("23","䷖",245,150,250,150,250,129),
         24: ("24","䷗",245,80,250,80,250,60),
         25: ("25","䷘",278,260,285,257,297,270),
         26: ("26","䷙",302,295,220,323,300,297),
         27: ("27","䷚",222,375,222,370,195,370),
         28: ("28","䷛",117,382,117,378,172,425),
         29: ("29","䷜",260,340,265,340,265,305),
         30: ("30","䷝",388,392,398,392,343,445),
         31: ("31","䷞",230,195,234,195,234,216),
         32: ("32","䷟",132,374,127,365,180,410),
         33: ("33","䷠",260,195,265,195,265,216),
         34: ("34","䷡",222,355,222,350,140,310),
         35: ("35","䷢",268,160,268,140,350,240),
         36: ("36","䷣",388,345,393,340,350,240),
         37: ("37","䷤",357,362,360,362,340,322),
         38: ("38","䷥",222,460,222,460,172,425),
         39: ("39","䷦",268,460,268,465,335,429),
         40: ("40","䷧",320,293,325,293,340,322),
         41: ("41","䷨",268,475,268,478,343,445),
         42: ("42","䷩",230,385,234,385,234,405),
         43: ("43","䷪",245,110,250,110,250,129),
         44: ("44","䷫",132,361,140,350,220,323),
         45: ("45","䷬",268,188,275,190,295,228),
         46: ("46","䷭",260,277,265,277,265,305),
         47: ("47","䷮",230,80,234,80,234,60),
         48: ("48","䷯",102,345,105,345,160,230),
         49: ("49","䷰",357,378,363,378,330,410),
         50: ("50","䷱",150,368,150,362,195,370),
         51: ("51","䷲",307,282,307,282,297,270),
         52: ("52","䷳",260,430,265,430,265,405),
         53: ("53","䷴",230,430,234,430,234,405),
         54: ("54","䷵",222,445,222,445,180,410),
         55: ("55","䷶",372,384,378,384,335,429),
         56: ("56","䷷",260,150,265,150,265,120),
         57: ("57","䷸",117,353,120,353,180,230),
         58: ("58","䷹",222,475,222,475,163,438),
         59: ("59","䷺",268,375,268,372,307,371),
         60: ("60","䷻",245,430,250,430,250,405),
         61: ("61","䷼",245,45,250,45,250,60),
         62: ("62","䷽",230,150,234,150,234,120),
         63: ("63","䷾",260,45,265,45,265,60),
         64: ("64","䷿",230,45,234,45,234,60) }

