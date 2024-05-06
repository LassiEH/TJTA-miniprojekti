*** Settings ***
Documentation    Testitapaukset author-luokalle
Resource    resource.robot

Library    BuiltIn

*** Test Cases ***
Testaa author-olion luonti
    ${testauthor}    Evaluate    author.Author("Testi Hahmo")
    Should Be Equal As Strings    ${testauthor}    Testi Hahmo

Testaa merkkijonoksi muuttaminen
    ${testauthor}    Evaluate    author.Author("Testi Henkilö")
    ${str}    Call Method    ${testauthor}    __str__
    Should Be Equal As Strings    ${str}    Testi Henkilö

Testaa apa-muotoinen merkkijono
    ${testauthor}    Evaluate    author.Author("Testi Tutkija")
    ${str}    Call Method    ${testauthor}    apastr
    Should Be Equal As Strings    ${str}    Tutkija, T.
