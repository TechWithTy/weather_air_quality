from enum import Enum


class UnitSystem(str, Enum):
    metric = "metric"
    imperial = "imperial"


class Language(str, Enum):
    en = "en"
    es = "es"
    fr = "fr"
    de = "de"


class PollenMapType(str, Enum):
    grass = "grass"
    tree = "tree"
    weed = "weed"
    overall = "overall"