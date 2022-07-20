"""
Module containing the Entity class.
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
                level=0,
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
            level: int
                The current level of this entity
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
        self.level = level
        self.entity_type = entity_type
        self.MAX_HEALTH = MAX_HEALTH
        self.mana = mana
        self.speed = speed
        self.accuracy = accuracy
        self.strength = strength
        self.magic = magic
        self.defense = defense

    def level_up(self) -> None:
        """
        Increases the entity object's level by one, 
        and stat increases by a factor of their current level

        Args:
        Returns:
            None
        Raises:
            None
        """
        if (self.level < 3):
            self.MAX_HEALTH += 200
            self.mana += 50
            self.speed += 2
            self.accuracy += 0.05
            self.magic += 0.05
            self.strength += 0.05
            self.defense += 0.1
        # Increase by a larger factor
        else:
            self.MAX_HEALTH += 500
            self.mana += 100
            self.speed += 5
            self.accuracy += 0.05
            self.magic += 0.1
            self.strength += 0.1
            self.defense += 0.1
        self.level += 1
