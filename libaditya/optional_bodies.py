"""Curated display-only Swiss Ephemeris objects (never added to graha sets)."""
from dataclasses import dataclass

import swisseph as swe


@dataclass(frozen=True)
class Body:
    name: str
    label: str
    swe_id: int
    abbreviation: str


BODIES = (
    Body('Chiron', 'Chiron', swe.CHIRON, 'Ch'),
    Body('Lilith', 'Black Moon Lilith (mean apogee)', swe.MEAN_APOG, 'Li'),
    Body('Ceres', 'Ceres', swe.CERES, 'Ce'),
    Body('Pallas', 'Pallas', swe.PALLAS, 'Pa'),
    Body('Juno', 'Juno', swe.JUNO, 'Ju'),
    Body('Vesta', 'Vesta', swe.VESTA, 'Ve'),
    Body('Eros', 'Eros (433)', swe.AST_OFFSET + 433, 'Er'),
    Body('Psyche', 'Psyche (16)', swe.AST_OFFSET + 16, 'Ps'),
    Body('Pholus', 'Pholus', swe.PHOLUS, 'Ph'),
    Body('Nessus', 'Nessus (7066)', swe.AST_OFFSET + 7066, 'Ne'),
)
BODY_BY_NAME = {body.name: body for body in BODIES}


class BodyUnavailable(KeyError):
    """An optional object has no ephemeris for this date/frame."""


from libaditya.objects.planets import Planet


class AdditionalBody(Planet):
    def dignity(self):
        return ''

    def abbreviation(self):
        return BODY_BY_NAME[self.identity()].abbreviation

    def is_outer_planet(self):
        return True


def calculate_body(name, context, master=None):
    body = BODY_BY_NAME[name]
    if name == 'Lilith' and context.sysflg >= 0 and context.sysflg & (swe.FLG_HELCTR | swe.FLG_BARYCTR):
        raise BodyUnavailable('Black Moon Lilith requires a geocentric or topocentric chart.')
    try:
        result = AdditionalBody(body.swe_id, context, master, display_name=name)
    except swe.Error as exc:
        raise BodyUnavailable(f'{body.label}: {exc}') from exc
    result._id = name
    return result
