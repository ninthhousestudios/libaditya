class Location:
    def __init__(
        self,
        lat=pglob.lat,
        long=pglob.long,
        alt=pglob.alt,
        placename=pglob.placename,
        timezone=pglob.timezone,
    ):
        self.lat = lat
        self.long = long
        self.alt = alt
        self.placename = placename
        self.timezone = timezone

    def __str__(self):
        return f"{self.placename} at ({self.lat},{self.long})\nelevation {self.alt} m\ntimezone: {self.timezone}"
