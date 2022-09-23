"""
This script creates a database for the gilded rose.
"""
import pathlib

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from gilded_rose.main import Item

ROOT_PATH = pathlib.Path(__file__).resolve().parent.absolute()

init_csv_path = ROOT_PATH / "data/gilded_rose_init.csv"
DB_PATH = ROOT_PATH / "data/gilded_rose.db"


def run_setup(database_path: pathlib.Path = DB_PATH):
    """Creates a database and fills it with the default initialisation data

    Arguments:
        database_path (pathlib.Path)
            The path under which the database must be saved
    """

    if database_path.exists():
        raise FileExistsError(
            "The database file already exists. Consider deleting it before running"
            "this script."
        )

    sqlite_path = f"sqlite:///{str(database_path)}"
    engine = sqlalchemy.create_engine(sqlite_path)
    SessionMaker = sessionmaker(bind=engine)
    session = SessionMaker()

    Item.metadata.create_all(engine)

    with open(init_csv_path) as f:
        for line in f.readlines()[1:]:
            name, sell_in, quality = line.strip().split(",")
            item = Item(name=name, sell_in=int(sell_in), quality=int(quality))
            session.add(item)
            session.commit()


if __name__ == "__main__":
    run_setup(database_path=DB_PATH)
