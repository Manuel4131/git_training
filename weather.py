#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ftime

def weather():
    city = "London"# Change Berlin to London
    print("Here is {}".format(city))
    print("Current date and time are {}".format(ftime.today()))

if __name__ == "__main__":
    weather()
