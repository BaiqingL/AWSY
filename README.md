# AWSY

Are.We.Secure.Yet is a framework that aims to mine data from BSSIDs. 

## Overview

AWSY aims to reveal the insecurity of public space. It uses captured BSSIDs to effectively pass through multiple APIs and mine potentially personal information. It is written in Python with supporting modules in Golang. 

## How it works

There are four main queries made in AWSY:

1. WiGLE.net/GoogleAPI can usually determine the **latitude and longitude** from a given BSSID.
2. GoogleAPI can use the latitude and longitude data to determine the **address** of the coordinates.
3. ZillowAPI can use the **address** to determine whether or not the property is a household.
4. EkataAPI can use the **address** to mine the names, historical addresses, phone numbers, associated people, and more about the residents.

## Usage

`./python AWSY.py <bssid>` 

Note that the bssid is given in the form AAAAAAAAAA without any colons. It is not case sensitive.

## Requirements

- `pyzillow`
- `pandas`
- `geopy`
- `pygle`

