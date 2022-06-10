import enum


class EntityType(enum):


class Entity():
    """
    Class declaration for an entity object
    An entity is any character in battle that has stats and a moveset

    Attributes:
        name: str
            The name associated with this entity object
        entity_type: EntityType
            Whether this entity is a hero, enemy, party member, or boss
        MAX_HEALTH: int
            The maximum amount of health points this entity can have
        mana: int
            The amount of energy this entity can expend on spells
        speed: int
            Determines the order that this entity will go in battle
        accuracy: double
            How likely an attack is going to hit
        strength: double 
            How many extra points go into physical attacks
        magic: double
            How many extra points go into magical attacks
        defense: double
            Determines how much damage this entity can withstand from enemies
            
    Functions:

    """
    def __init__(self) -> None:
        pass