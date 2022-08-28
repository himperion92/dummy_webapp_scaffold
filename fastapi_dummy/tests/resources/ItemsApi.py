from requests import Session

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

class ItemRetrievalError(Exception):
    """
        Exception raised whenever there is an error retrieving an item
    """

class ItemsApi:
    
    ROBOT_LIBRARY_SCOPE='SUITE'
    
    def __init__(self, url) -> None:
        self.url = url
        self.session = Session()

    @keyword('Get Item')
    def get_item(self, item_id: int) -> dict:
        response = self.session.get(f"{self.url}/items/{item_id}")
        if response.status_code == 200:
            return response.json()
        else:
            raise ItemRetrievalError(f"Error {response.status_code} when retrieving item with ID '{item_id}'")

    @keyword('Verify Item ID')
    def check_id_of_item(self, item: dict, expected_id: int):
        BuiltIn().should_be_equal_as_numbers(item['item_id'], expected_id)

    @keyword('Perform An Incorrect Request')
    def perform_incorrect_request(self) -> int:
        response = self.session.get(f"{self.url}/incorrect_endpoint")
        return response.status_code