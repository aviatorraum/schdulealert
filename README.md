## Problem
Need a reminder to notify colleague so that he/she will not miss the train.

## Solution
A schedule alert will pop-up alert message on the desktop when it's time to leave.

## How to run this script
1. Double click "SchduleAlert.py".
2. Enter expect leave time with the format "HH:MM:SS".

## Requirement
Python 3.6.2

## Design thinking
The first idea is to create a script to get current coordinate then obtain arrive time and destination from user.
With APIs from VBB allows getting the information of the best route.
A pop-up message remains user to leave the office.
But when I tried to get current coordinate, the responded coordinate always near Berliner Dom so that I changed the way to create a simple alert script.
Which only need to enter a expect leave time.
Then problem solved.
