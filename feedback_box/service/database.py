from uuid import uuid4

from feedback_box.domain.tripcode import Tripcode
from feedback_box.persistance.database_services.memory_database_service import MemoryDatabaseService

inbox_1 = {
        'id': str(uuid4()),
        'owner': 'first_owner',
        'tripcode': Tripcode().generate_code(owner='first_owner', password='dummy_password'),
        'question': 'Do you like me?'
    }


inbox_2 = {
        'id': str(uuid4()),
        'owner': 'second_owner',
        'tripcode': Tripcode().generate_code(owner='second_owner', password='dummy_password'),
        'question': 'Do you like icecream?'
    }


db = MemoryDatabaseService([inbox_1, inbox_2])

