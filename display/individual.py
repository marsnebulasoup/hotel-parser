######################
# Name: Kevin Bryniak
# Final Project
# Generates individual hotel statistics.
######################

from pandas import Series
from consts.aggregate import (
    DEFAULT_UNKNOWN_MSG,
    REVIEW_COUNT_COL,
    ROOM_COL,
    SCORE_COL,
    STARS_COL,
)
from rich.panel import Panel
from rich.text import Text

from consts.display import SCORE_TEXT, STAR_TEXT


def get_value(hotel: Series, key: str):
    value = DEFAULT_UNKNOWN_MSG

    if type(hotel) is Series and type(key) is str:
        if key in hotel:
            if hotel[key] != -1:
                value = hotel[key]

    return value


def try_round(number, precision=None):
    try:
        number = round(float(number), precision)
    except:
        pass
    return number


def generate_hotel_panel(hotel: Series):
    text = Text()

    if type(hotel) is Series:
        score = try_round(get_value(hotel, SCORE_COL), 2)
        review_count = try_round(get_value(hotel, REVIEW_COUNT_COL))
        stars = try_round(get_value(hotel, STARS_COL))
        rooms = try_round(get_value(hotel, ROOM_COL))

        text.append(f"{SCORE_COL}: {score}{SCORE_TEXT}")
        text.append(f"\n{STARS_COL}: {stars}{STAR_TEXT}")
        text.append(f"\n{REVIEW_COUNT_COL}: {review_count}")
        text.append(f"\n{ROOM_COL}: {rooms}")

    panel = Panel(text, title=str(hotel.name))

    return panel
