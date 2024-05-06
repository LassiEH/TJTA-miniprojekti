*** Settings ***
Documentation    Testitapaukset ref-luokan ja references-luokan toiminnalle
Resource         resource.robot

Library    Collections
Library    String
Library    BuiltIn

*** Test Cases ***
Testaa ref-luokka oikealla datalla
    [Documentation]    Testaa, että ref-luokka toimii oikealla datalla
    [Tags]             init    ref

    ${ref}    Artikkeli datalla

    Should Be Equal As Strings    ${ref}    John Smith. Test title: a case study: Journal on testing, 2. 1-3, 2024

Testaa ref-luokka tyhjillä tekijöillä
    [Documentation]    Testaa, että ref-luokka ei tallenna, jos syötteessä ei ole kirjoittajaa
    [Tags]             init    ref
    
    ${ref}    Artikkeli rikkinäisellä datalla
    Should Be Equal As Strings    ${ref}    None

Testaa references-luokan lisäys- ja tekstiksi muuttamisen metodit
    [Documentation]    Testaa, että Ref-olio voidaan lisätä References-olioon
    [Tags]             references
    
    ${ref}    Artikkeli datalla
    ${references}    Evaluate    references.References()
    Call Method    ${references}    lisaaLahde    ${ref}
    ${text}    Call Method    ${references}    toString
    Should Be Equal As Strings   ${text}    John Smith. Test title: a case study: Journal on testing, 2. 1-3, 2024

Testaa tyhjän references-olion tulostaminen
    [Documentation]    Testaa, että tyhjä references olio tulostaa oikein
    [Tags]             references

    ${references}    Evaluate    references.References()
    ${text}    Call Method    ${references}    toString
    Should Be Equal As Strings    ${text}    Lähteitä ei ole.


        
    

*** Keywords ***

Artikkeli datalla
    ${author}       Create List     John Smith
    ${title}        Set Variable    Test title: a case study
    ${journal}      Set Variable    Journal on testing
    ${year}         Set Variable    2024
    ${volume}       Set Variable    2
    ${pages}        Set Variable    1-3
    ${userkeys}     Set Variable    testkey1

    ${ref}          Evaluate    ref.Ref($author, $title, $journal, $year, $volume, $pages, $userkeys)
    [Return]        ${ref}

Artikkeli rikkinäisellä datalla
    ${author}       Create List     
    ${title}        Set Variable    Test title: a case study
    ${journal}      Set Variable    Journal on testing
    ${year}         Set Variable    2024
    ${volume}       Set Variable    2
    ${pages}        Set Variable    1-3
    ${userkeys}     Set Variable    testkey1

    ${ref}          Evaluate    ref.Ref($author, $title, $journal, $year, $volume, $pages, $userkeys)
    [Return]        ${ref}
