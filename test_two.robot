*** Settings ***
Documentation       Test Cases using Robot Framework
Library     historical_ll_lib.py

# *** Variables ***
# ${SUCCESS}      True

*** Keywords ***
getfirstvalue
  ${firstvalue} =  testone
  [Return]  ${firstvalue}

getsecondvalue
  ${secondvlaue} =  testtwo
  [Return]  ${secondvlaue}

getdi
  [Arguments]  ${START}  ${END}  ${LOC}
  ${rows} =  get di rows  ${START}  ${END}  ${LOC}
  [Return]  ${rows}

getdb
  ${rows} =  get db rows
  [Return]  ${rows}

*** Test Cases ***
comparevalues
  ${firstresult} =  getfirstvalue
  ${secondresult} =  getsecondvalue
  Should Be Equal  ${firstresult}  ${secondresult}

comparerows
  ${db} =  getdb
  ${di} =  getdi  2019-06-01  2019-07-01  NM 
  Should Be Equal  ${db}  ${di}