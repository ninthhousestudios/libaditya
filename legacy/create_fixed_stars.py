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

from libaditya.stars.fixed_stars import TheStars

def main():

    thestars = TheStars()

    with open("stars.py","w") as fd:
        lines = []
        for key,value in thestars.the_stars().items():
            line = ""
            name = value.replace(" ","")
            name = value.replace("'","")
            if not name:
                name = key
            if any(char.isnumeric() for char in name):
                # name has any numbers, they are at the beginning of the name
                # so put them at the end; i did this manually for stars/the_stars.py
                # now get the numbers and move them to the end
                if name[:3].isnumeric():
                    name = name[3:]+name[:3]
                if name[:2].isnumeric():
                    name = name[2:]+name[:2]
                if name[:1].isnumeric():
                    name = name[1:]+name[:1]
            if any(char.isnumeric() for char in key):
                # key has any numbers, they are at the beginning of the key
                # so put them at the end; i did this manually for stars/the_stars.py
                # now get the numbers and move them to the end
                if key[:3].isnumeric():
                    key = key[3:]+key[:3]
                if key[:2].isnumeric():
                    key = key[2:]+key[:2]
                if key[:1].isnumeric():
                    key = key[1:]+key[:1]
            name = name.replace("-","")
            name = name.replace(".","")
            line += f"class {name}(FixedStar): # ,{key}\n\n"
            line += f"    def __init__(self, context = EphContext):\n"
            line += f"        super().__init__(swe_id = \",{key}\", context=context)\n\n"
            lines.append(line) 
        fd.writelines(lines)

if __name__ == "__main__":
    main()
