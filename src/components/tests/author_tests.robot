*** Settings ***
Documentation    Testitapaukset author-luokalle
Library    ../author.py

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
    ${testauthor}    Evaluate    author.Author("Testi", "Tutkija")
    ${str}    Call Method    ${testauthor}    apastr
    Should Be Equal As Strings    ${str}    Testi, T.

    ${testiauthor}    Evaluate    author.Author("Sukunimi")
    ${string}    Call Method    ${testiauthor}    apastr
    Should Be Equal As Strings    ${string}    Sukunimi

Testaa bibtex-muotoinen merkkijono
    ${testauthor}    Evaluate    author.Author("Testaaja", "Yksi")
    ${str}    Call Method    ${testauthor}    bibtexstr
    Should Be Equal As Strings    ${str}    Testaaja, Yksi

    ${testauthor}    Evaluate    author.Author("Testaaja")
    ${str}    Call Method    ${testauthor}    bibtexstr
    Should Be Equal As Strings    ${str}    Testaaja
