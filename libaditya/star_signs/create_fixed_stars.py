
from libaditya.star_signs.fixed_stars import TheStars


def main():

    thestars = TheStars()

    with open("stars.py","w") as fd:
        lines = []
        for key,value in thestars.the_stars().items():
            line = ""
            name = value.replace(" ","")
            if not name:
                name = key
            name = name.replace("-","")
            name = name.replace(".","")
            line += f"class {name}(FixedStar):\n\n"
            line += f"    def __init__(self, context = EphContext):\n"
            line += f"        super().__init__(swe_id = \",{key}\", context=context)\n\n"
            lines.append(line) 
        fd.writelines(lines)

if __name__ == "__main__":
    main()
