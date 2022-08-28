*** Settings ***
Library  ../resources/ItemsApi.py  %{SERVER_URL}


*** Variables ***
${ITEM_ID} =  350


*** Test Cases ***
Get an specific item
    [Tags]  Functional  Nominal
    When A Get Request Is Executed To The API
    Then The Expected ID Is Returned

Perform a request to an incorrect endpoint
    [Tags]  Functional  Abnormal
    When A Request Is Executed To An Unexisting Endpoint
    Then The Expected 404 Error Should Be Returned


*** Keywords ***
A Get Request Is Executed To The API
  ${item} =  Get Item  ${ITEM_ID}
  Set Test Variable  ${item}

The Expected ID Is Returned
    Verify Item ID  ${item}  ${ITEM_ID}

A Request Is Executed To An Unexisting Endpoint
    ${status_code} =  Perform An Incorrect Request
    Set Test Variable  ${status_code}

The Expected ${http_code} Error Should Be Returned
    Should Be Equal As Integers  ${status_code}  ${status_code}