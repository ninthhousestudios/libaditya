# former method fro class stars.the_stars.TheStars()

# requires an argument
# stars_file=const.stars_file
# this was from the process of bootstrapping
    def stars_strdict(self):
        """
        here we take self._the_stars_lines and create a dictionary
        "nomenclature_nature": "traditiona_name" -> self._the_stars
        """
        with open(self.stars_file,"r") as stars_fd:
            the_stars_lines = dict() 
            the_lines = stars_fd.readlines()
            for n,line in enumerate(the_lines):
                if "#" in line:
                    # a comment, continue
                    continue
                the_stars_lines[n] = line
            self._the_stars_lines = the_stars_lines
        the_stars = dict()
        for line in self._the_stars_lines.values():
            parts = line.split(",")
            # nomenclature is second, traditional is first in the file
            name = parts[0]
            if name.replace(" ","") == "":
                # if the name is empty
                # make the key into the name
                name = parts[1]
                # manipulate it to be consistent
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
            # this line sets the key value pair in the dictionary
            the_stars[parts[1]] = name
        return the_stars

def original_repr_Varga():
    """
    this is for every varga except the Rashi
    the rashi is printed with nakshatras
    the others are not

    str prints a table with signs at the top
    each object is printed under its sign
    as "object in_sign_longitude"
    the number of rows will be equal to the most objects that are in one sign

    changed this to return mkheader(), to just see what it is, an id of sorts
    """
    output = PrettyTable()
    # list of the sign names
    output.field_names= list([sign for sign in [self.context.names.sign_names]][0])

    # get the sign with the most objects, so we know how many rows to print
    rows = self._signs.most_objects()

    for r in range(0,rows):
        # construct the row
        row = []
        # could also write for s in self._signs.signs().values()
        # and then replace self._signs[s]._objects by s._objects
        for s in self._signs.keys():
            if len(self._signs[s]._objects) > r:
                if not self.context.print_outer_planets and self._signs[s]._objects[r].object_type()=="Planet" and self._signs[s]._objects[r].is_outer_planet():
                    row.append("")
                    continue
                if self._signs[s]._objects[r].identity() == "Sun" and self.context.sysflg == const.HELIO:
                    # dont print the Sun is using heliocentric coordinates
                    row.append("")
                    continue
                rowstr = f"{self._signs[s]._objects[r].name()}\n{self._signs[s]._objects[r].in_sign_longitude()}\n"
                # if this is a Rashi, print nakshatras, if that is specified
                # unless it is barycentric or heliocentric
                if isinstance(self,Rashi) and (self.context.sysflg != const.BARY and self.context.sysflg != const.HELIO):
                    # print nakshatras or not
                    if self.context.print_nakshatras:
                        rowstr += f"{self._signs[s]._objects[r].nakshatra_name()}\n{self._signs[s]._objects[r].nakshatra().elapsed()}\n"
                row.append(rowstr) 
            else:
                row.append("")
        output.add_row(row)

    ret = output.get_string(fields=list([sign for sign in [self.context.names.sign_names]][0]))


# originally i passed the names around to every function and every object

#@dataclass(frozen=True)
#class Names:
#    planet_names: str = tuple(const.planet_names)
#    sign_names: str = tuple(const.adityas)
#    nakshatras: str = tuple(const.nakshatras)
#    tithis: str =  tuple(const.tithis)
#    karanas: str = tuple(const.karanas)
#    varas: str = tuple(const.varas)
#    yogas: str = tuple(const.yogas)
#    adityas: str = tuple(const.adityas)
#    zodiac: str = tuple(const.zodiac)
