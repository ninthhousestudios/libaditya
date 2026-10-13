# RemoteControl is the package StellariumRC
# i changed the class Stellarium to RemoteControl, that is the only difference
# i copied and pasted the one directory of code into remote_control
# the license is mit, even though known of the file have the license in them

from . import main,objects,scripts,simbad,stelaction,stelproperty,location,locationsearch,view

class RemoteControl:
    def __init__(self, ip="127.0.0.1", port=8090, password="") -> None:
        self.password = password
        self.ip = ip
        self.port = port
        self.main = main.Main(self.ip, self.port, self.password)
        self.objects = objects.Objects(self.ip, self.port, self.password)
        self.scripts = scripts.Scripts(self.ip, self.port, self.password)
        self.simbad = simbad.Simbad(self.ip, self.port, self.password)
        self.stelaction = stelaction.StelAction(self.ip, self.port, self.password)
        self.stelproperty = stelproperty.StelProperty(self.ip, self.port, self.password)
        self.location = location.Location(self.ip, self.port, self.password)
        self.locationsearch = locationsearch.LocationSearch(self.ip, self.port, self.password)
        self.view = view.View(self.ip, self.port, self.password)
        
