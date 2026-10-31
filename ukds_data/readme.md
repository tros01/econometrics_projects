# Working with UK Data Service datasets

I have always found navigating [UKDS](https://ukdataservice.ac.uk/) datasets difficult. The datasets are large and unwieldy. Extracting files can be tedious and draining. In this project, I define some helpers to make the job of locating, recoding and renaming variables automatable.

In **Python**, I construct some functions to list files in a zip archive and to extract individual files. Two other useful functions parse the archived data dictionary and construct a Python dictionary mapping variables onto column locations and variable labels, and another Python dictionary mapping variables onto the respective dictionaries of code and label pairs.

An **R** script is being made and will be up shortly.

This is by no means a comprehensive project but rather an archive of useful helpers that hopefully make working with UKDS datasets such as the **Labour Force Survey** and **Understanding Society** a bit easier.
