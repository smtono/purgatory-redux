import enum


class EntityType(enum):
    """
    Describes the kind of entity that is represented by an object
    """

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
    def __init__(self, 
                name="", 
                entity_type=None, 
                MAX_HEALTH=300, 
                mana=50, 
                speed=10, 
                accuracy=0.6, 
                strength=0.0, 
                magic=0.0, 
                defense=0.0) -> None:
        """
        Initializes an Entity object

        Args:
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
        Returns:
            None
        Raises:
            None
        """
        self.name = name
        self.entity_type = entity_type
        self.MAX_HEALTH = MAX_HEALTH
        self.mana = mana
        self.speed = speed
        self.accuracy = accuracy
        self.strength = strength
        self.magic = magic
        self.defense = defense