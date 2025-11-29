from datetime import datetime
from sqlalchemy import DateTime
from library.create_tables import init_db
import random 
from library.services import (
    create_author, update_author, delete_author,
    get_all_authors, 
)
from library.db import get_db

init_db()

#print(create_author("Cho'lpon", "Kecha va kunduz"))

#print(update_author(1, "Abdulla Qodiriy", "O'tkan kunlar"))

#print(delete_author(2))

#print(get_all_authors())
