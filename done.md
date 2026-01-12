#
2025/12/01: I did this and then pyphemeris didn't print correctly!
change Signs.__str__ and Signs.__repr__
it is now changed back. don't change again unless doing a complete overhaul.

#
2025/12/01 - done
split pyphemeris off from libaditya

i changed pyproject.toml to use hatch
it built and published libaditya correctly, with all the ephe files; it works, i checked
it
it didnt include pyphemeris because i didnt tell it to
so then i can just move pyphemeris
