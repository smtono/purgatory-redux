class GameObject(pygame.sprite.Sprite):
    """
    Any object represented by a sprite in the overworld of the game

    Attributes:
        is_collideable: boolean
            Describes whether this object has collision detection with the player object
        image: pygame.Surface
            A drawing or sprite that represents the Entity character
        rect: pygame.Rect
            The Rect object associated with the sprite image in pygame
    
    Functions:
        get_rect()
            Returns the rect object of the sprite
    """
