
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
