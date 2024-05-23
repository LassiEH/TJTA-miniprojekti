*** Settings ***
Documentation    Robottitesti ajaa pythonilla luodut testicaset
Library    Process

*** Test Cases ***
Viitteisiin liittyvä toiminnallisuus
    Run Process  python  .ref_test.py

Power user toiminnallisuus
    Run Process    python    .poweruserUI_test.py

Käyttöliittymän toiminnallisuus
    Run Process    python    .cli_test.py
