"""
Elemental stuff
"""
from enum import Enum, auto


class Element(Enum):
    NONE = auto()
    LIGHT = auto()
    DARK = auto()
    ELECTRIC = auto()
    FIRE = auto()
    WATER = auto()
    EARTH = auto()
    AIR = auto()
    METAL = auto()
    ACID = auto()
    PSYCHIC = auto()
    WEIRD = auto()

ELEMENT_WEIGHTS = [
    130,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
]


LIGHT_WORDS = [
    'light',
    'flash',
    'solar',
    'luminous',
    'bright',
    'glowing',
    'radiant',
    'resplendent',
    'vivid',
    'flourescent',
    'scintillant',
    'shiny'
 ]

DARK_WORDS = [
    'dark',
    'void',
    'darkened',
    'moon',
    'lunar',
    'black',
    'obscure',
    'dull',
    'shadowy',
    'nebulous',
    'stygiandeprived',
    'barren',
    'vacant',
    'devoid'
 ]

ELECTRIC_WORDS = [
    'electric',
    'thunder',
    'shock',
    'spark',
    'volt',
    'jolting',
    'shockwave',
    'electrosurge',
    'thunderbolt',
    'voltaic'
 ]

FIRE_WORDS = [
    'fire',
    'blazing',
    'hot',
    'fiery',
    'searing',
    'piping',
    'igneous',
    'sizzling',
    'scorching',
    'scalding',
    'blistering',
    'burning'
 ]

WATER_WORDS = [
    'water',
    'wet',
    'drenched',
    'dank',
    'misty',
    'soaked',
    'soaked',
    'watery',
    'soppy',
    'damp',
    'soggy',
    'dewy',
    'drippy',
    'oozy',
    'moist',
    'sodden',
    'freezing',
    'ice',
    'icy',
    'cold',
    'frost',
    'frosty',
    'frozen',
    'snowy'
 ]

EARTH_WORDS = [
    'earth',
    'grass',
    'stone',
    'earthen',
    'viny',
    'flowery',
    'wood',
    'wooden',
    'ground',
    'mossy',
    'grassy',
    'stony',
    'dusty',
    'overgrown',
    'thorny',
    'slimy',
    'moldy'
 ]

AIR_WORDS = [
    'air',
    'windy',
    'wind',
    'breezy',
    'drafty',
    'tornado',
    'airy',
    'breathy',
    'wafty',
    'sky',
    'zephyr',
    'wispy',
    'gusty',
    'gale',
    'gustful',
    'whirlwind',
    'fluttery',
    'tempest',
    'turbulent',
    'tumultuous',
    'tempestuous',
    'howling',
    'roaring'
 ]

METAL_WORDS = [
    'metal',
    'iron',
    'steel',
    'alloy',
    'galvanized',
    'forged',
    'plated',
    'titanium',
    'zinc',
    'copper',
    'bronze',
    'adamantine',
    'mithral',
    'platinum',
    'electrum',
    'gold',
    'brass',
    'silver',
    'aluminum',
    'nickel',
    'foil',
    'rusty'
 ]

ACID_WORDS = [
    'acid',
    'acidic',
    'caustic',
    'abrasive',
    'corroding',
    'acrid',
    'mordant',
    'disintegrative',
    'dissolving',
    'corrosive',
    'gnawing'
 ]

PSYCHIC_WORDS = [
    'psychic',
    'mental',
    'phasing',
    'phasic',
    'mystic',
    'occult',
    'psychotic',
    'cerebral',
    'sentient',
    'telekinetic',
    'telepathic',
    'psychogenic',
    'subliminal',
    'phrenic',
    'rational',
    'intelligent',
    'studious'
 ]

WEIRD_WORDS = [
    'weird',
    'strange',
    'odd',
    'peculiar',
    'unknown',
    'unnatural',
    'oddball',
    'mysterious',
    'uncanny',
    'curious',
    'eccentric',
    'freaky',
    'kooky',
    'outlandish'
 ]

ELEMENT_DICT = {
    Element.NONE: [""],
    Element.LIGHT: LIGHT_WORDS,
    Element.DARK: DARK_WORDS,
    Element.ELECTRIC: ELECTRIC_WORDS,
    Element.FIRE: FIRE_WORDS,
    Element.WATER: WATER_WORDS,
    Element.EARTH: EARTH_WORDS,
    Element.AIR: AIR_WORDS,
    Element.METAL: METAL_WORDS,
    Element.ACID: ACID_WORDS,
    Element.PSYCHIC: PSYCHIC_WORDS,
    Element.WEIRD: WEIRD_WORDS
}