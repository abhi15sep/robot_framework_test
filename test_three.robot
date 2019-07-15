*** Settings ***
Documentation       Test Cases using Robot Framework
Test Template       testlen
Library     historical_ll_lib.py

*** Variables ***
${SUCCESS}      True

*** Keywords ***
testlen
    [Arguments]     ${START}    ${END}  ${LOC}   
    validation      ${START}    ${END}  ${LOC}

*** Test Cases ***
validaterows     2019-06-01      2019-07-01      NM  