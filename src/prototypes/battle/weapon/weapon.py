"""

"""
import enum
import string

class WeaponType(enum):
    """
    The kind of attacking style associated with the weapon
    """

    # physical
    # magical
    # support

class Weapon():
    """
    The tool used by the player and entities to attack each other in battle

    Args:
        name: string
            What the weapon is called
        result: int
            The attack power / healing power that this weapon has 
        mana: int
            How much power / energy is consumed by using this weapon
        accuracy: float 
            Determines how likely the weapon will hit another entity
        isAffectAll: boolean
            Determines if this weapon can attack multiple enemies at once
        levelOfAccess: int
            The level the entity has to be to access this weapon
    Returns:
        None
    Raises:
        None
    """
    def __init__(name: string, 
                result: int, 
                mana: int, 
                accuracy: float, 
                isAffectAll: bool, 
                levelOfAccess: int) -> None:
        """_summary_

        Args:
            name (string): _description_
            result (int): _description_
            mana (int): _description_
            accuracy (float): _description_
            isAffectAll (boolean): _description_
            levelOfAccess (int): _description_
        """
        pass
