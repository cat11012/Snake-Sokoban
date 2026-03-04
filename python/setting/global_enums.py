from enum import Enum

class Colors(Enum):
    BLUE = "blue"
    BRIGHT_DARK_BLUE = "bright_dark_blue" 
    BRIGHT_GREEN_BLUE = "bright_green_blue"
    BRIGHT_GREEN = "bright_green"
    BRIGHT_LIGHT_BLUE = "bright_light_blue"
    BRIGHT_ORANGE = "bright_orange"
    BRIGHT_RED = "bright_red"
    BRIGHT_YELLOW = "bright_yellow"
    DARK_BLUE = "dark_blue"
    DARK_GREEN = "dark_green"
    DARK_ORANGE = "dark_orange"
    DARK_RED = "dark_red"
    DARK_YELLOW = "dark_yellow"
    GREEN = "green"
    PINK = "pink"
    PURPLE = "purple"
    SILVER_GELATIN = "silver_gelatin"

class InterfaceStatus(Enum):
    LOADING = "loading"
    LOBBY = "lobby"
    LEVEL_SELECTION = "level_selection"
    GAMEPLAY = "gameplay"
    LEVEL_COMPLETE = "level_complete"
    NONE = "none"

