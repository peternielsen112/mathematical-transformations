# Mathematical Transformations in Python

[![Github All Releases](https://img.shields.io/github/downloads/peternielsen112/mathematical-transformations/total.svg)](https://github.com/peternielsen112/mathematical-transformations/releases)
[![GitHub release](https://img.shields.io/github/release/peternielsen112/mathematical-transformations/all.svg)](https://github.com/peternielsen112/mathematical-transformations/releases)
[![GitHub Release Date](https://img.shields.io/github/release-date-pre/peternielsen112/mathematical-transformations.svg)](https://github.com/peternielsen112/mathematical-transformations/releases)
[![GitHub license](https://img.shields.io/github/license/peternielsen112/mathematical-transformations)](https://github.com/peternielsen112/mathematical-transformations/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/peternielsen112/mathematical-transformations.svg)](https://github.com/peternielsen112/mathematical-transformations/stargazers)

### Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Multiple Point Transformations](#multiple-point-transformations)
  - [Dilation](#dilation)
- [Single Point Transformations](#single-point-transformations)
  - [Reflection](#reflection)
  - [Rotations](#rotations)
  - [Translations](#translations)
- [About the Creator](#about-the-creator)

---
## Overview

This repository contains four programs: dilations.py, reflections.py, rotations-singlepoint.py, and translations-singlepoint.py. Each one is meant to reproduce a form of transformation within algebraic geometry. Two of the programs enable transformations applying to a three-point shape - a triangle - and the other two enable transformations applying to a single point. **None of these programs show a coordinate plane.** I am currently working on turning these functions into a Python module for ease of access.

---
## Requirements
These four programs require Python 3.7 or higher. No modules are required for the use of these programs.

---
## Multiple Point Translations

The program dilations.py is used for three points (often in the form of a triangular shape).

### Dilation

The program dilations.py is run from the command line using `python3 dilations.py`. You will be prompted for a scale factor of the dilation (which should be nonnegative).  You will also be prompted for the x and y values of three points. The program will return the dilation of those points with the given scale factor.

---
## Single Point Transformations

The three programs reflections.py, rotations-singlepoint.py, and translations-singlepoint.py are used for one point.

### Reflection

The program reflections.py is run from the command line using `python3 reflections.py`. You will be prompted for the axis of reflection - x or y - and the coordinates of the point. The program will return the reflected point's coordinates.

### Rotation

The program rotations-singlepoint.py is run from the command line using `python3 rotations-singlepoint.py`. You will be prompted for the degree value of the rotation: 90, 180, or 270 (the angle of 360 would be the original point). Then you will be asked to input the x- and y-coordinates of the point. The rotation will then occur at the angle specified around the origin.

### Translation

The program translations-singlepoint.py is run from the command line using `python3 translations-singlepoint.py`. You will be prompted to enter the current coordinates of the point and then the direction of change for x (left/right) and the number of units right or left. Then you will be prompted to enter the direction of change for y (up or down) and the number of units up or down. The program will return the coordinates of the point after the specified translation.

## About the Creator

I create programs in a variety of languages, from Python to JavaScript to CSS and more. I'm on GitHub: [@peternielsen112](https://github.com/peternielsen112) and also [Replit.com](https://replit.com/@peternielsen112) by the same username.
Please email any problems or suggestions to me at <dirigo112@gmail.com>.