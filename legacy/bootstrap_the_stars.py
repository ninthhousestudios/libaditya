# _bootstrap_the_stars generate the natural_stars dictionary in the_stars.py
# this is a dictionary of ",noMen": constructor type
# you can access is through TheStars like this:
# >>> TheStars()[",noMen"]()

# below is paths for bootstrapping

# stars_path = os.path.dirname(os.path.realpath(__file__))
# the_stars_file = stars_path + "/the_stars.py"

#    def _bootstrap_the_stars(self):
#        """
#        here we take self._the_stars_lines and create a dictionary
#        "nomenclature_nature": "traditiona_name" -> self._the_stars
#
#        the_stars_file (.../stars/the_stars.py) has all the FixedStar classes for each star
#        read just the name of each class and pass as a dictionary key to use as a constructor
#
#        if you run this again it will append to the_stars.py, so dont unless you really want to fix
#        some errors by hand. there werent to many, but the scripts did miss somethings
#        """
#        input("Do you really want to bootstrap the files? It will append to ./the_stars.py:")
#        with open(self.python_stars,"r") as starsfd:
#            lines = starsfd.readlines() 
#        the_stars = dict()
#        for line in lines:
#            if not "class" in line:
#                continue
#            # line has the form: class Name(FixedStar): # ,noMen (clature name)
#            value = line.split(" ")[1].split("(")[0]
#            key = line.split(" ")[3].strip()
#            the_stars[key] = value
#        # now we need to write a python file that can be loaded into the interpreter
#        # it is a dictionary like libaditya.objects.natural_planets
#        # "natural" here means "natural to python"; the value are constructors
#        # so you can do natural_planets["Sun"](), which is the same as Sun()
#        # I want to do that with fixed stars. There are 1113 named stars, so we are
#        # using python to "bootstrap" being to use all these classes easily
#        # eventually, TheStars()["alTau"] will return an "Aldebaran" class
#        lines = []
#        lines.append("natural stars = {\n")
#        for key,constructor in the_stars.items():
#            lines.append(f'    "{key}": {constructor},\n')
#        lines.append("}\n")
#        with open(self.python_stars,"a") as starsfd:
#            starsfd.writelines(lines)
#        return the_stars

