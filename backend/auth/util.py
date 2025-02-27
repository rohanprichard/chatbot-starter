from .model import UserInformation
from typing import Dict, Any


def get_user_information(information: UserInformation) -> Dict[str, Any]:
    return information.model_dump()
