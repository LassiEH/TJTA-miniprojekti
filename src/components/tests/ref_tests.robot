*** Settings ***
Documentation    Testitapaukset ref-luokan toiminnalle
Resource         resource.robot

Library    OperatingSystem

*** Test Cases ***
Testaa ref luokka oikealla datalla
    [Documentation]    Testaa, että ref luokka toimii oikealla datalla
    [Tags]             init

    ${author}       Create List     John Smith    Jane Doe
    ${title}        Set Variable    Test title: a case study
    ${journal}      Set Variable    Journal on testing
    ${year}         Set Variable    2024
    ${volume}       Set Variable    2
    ${pages}        Set Variable    1-3
    ${userkeys}     Set Variable    testkey1

    ${ref}          Evaluate    ref.Ref($author, $title, $journal, $year, $volume, $pages, $userkeys)
    Should Be Equal As Strings    ${ref}    John Smith, Jane Doe. Test title: a case study: Journal on testing, 2. 1-3, 2024
