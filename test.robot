*** Settings ***
Documentation       Excersie Test Cases using Robot Framework
Test Template       testlogin
Library             LoginLibrary.py

*** Variables ***
${SUCCESS}      /var/folders/v7/qdy0ksh163d66phpg6htg1kjcyxqr2/T/robotframework-quickstart-db.txt

*** Test Cases ***  USERNAME    PASSWORD
TestCreateUser      kristans    123Abcd

*** Keywords ***
testlogin
    [Arguments]     ${USERNAME}     ${PASSWORD}
    create user     ${USERNAME}     ${PASSWORD}
    status should be    SUCCESS\n${SUCCESS}