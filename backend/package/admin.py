from typing import Dict
from uuid import uuid4

from flask import Request

from .models import PersonInfo


def process_person_info(request: Request) -> Dict[str, str]:
    pesron_info = PersonInfo(**{
        'id': str(uuid4()),
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
    })
    return pesron_info.model_dump()
