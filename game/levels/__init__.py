import importlib
import pkgutil
import game


def walk_levels(room_1, room_2):
    for module in pkgutil.walk_packages(
        game.levels.__path__,
        f"{game.levels.__name__}.",
    ):

        level = importlib.import_module(module.name)
        yield level.build_level(room_1, room_2)


def get_level(id, room_1, room_2):
    return importlib.import_module(f"{game.levels.__name__}.{id}").build_level(
        room_1, room_2
    )
