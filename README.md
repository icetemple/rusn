## rusn

[![Build Status](https://travis-ci.org/icetemple/rusn.svg?branch=master)](https://travis-ci.org/icetemple/rusn)
[![Coverage Status](https://coveralls.io/repos/github/icetemple/rusn/badge.svg?branch=master)](https://coveralls.io/github/icetemple/rusn?branch=master)

Small library for getting russian text with singular and plural forms


## Instalation

`pip install --user rusn`


## Example


    apple_forms = ['яблоко', 'яблока', 'яблок']
    
    rusngettext(1, apple_forms)
    >> 'яблоко'

    rusngettext(10, apple_forms)
    >> 'яблок'
