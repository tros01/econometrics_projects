# Working with UK Data Service datasets

[UKDS](https://ukdataservice.ac.uk/) datasets such as the **Labour Force Survey** and **Understanding Society** can be difficult to navigate. Locating, recoding and renaming variables can be challenging because the documentation is online or in inaccessible rtf files. Extracting files and searching for compatible datasets can also be problematic. The set of functions in this (evolving) project aims to make the automation of at least some of these tasks a touch more accessible. The functionality in **Python** and **R** is, to all intents and purposes, identical.

## Getting the UKDS data

UKDS surveys are available from the [UK Data Service](https://ukdataservice.ac.uk/). I have no permission to disseminate the datasets. Anybody interested must register with the service and download the files directly.

## These notebooks

The **Labour Force Survey** and **Understanding Society** datasets are standardised, and the data dictionaries are stored in a nested zip file. All functionality in the notebooks has been tested on the original LFS zip archives containing tab-delimited files and is loop-ready.

The notebooks contain
* archive itemising functions (for those who do not extract the original UKDS files but want a list of contents)
* file extractors (for those who would like to unzip specific files)
* variable itemising functions (data dictionary extractors mapping variable names onto column position and variable labels)
* code itemising functions (data dictionary extractors mapping variable names onto variable-specific code-label pairs)
* `read_tab` functions in `tidyverse` with `janitor`-cleaned variable names compatible with the variable and code lists
* `read_tab` functions in `pandas` and `polars` with `skimpy`-cleaned variable names compatible with the variable and code dictionaries

Note that some generic Python functionality has been hived off into a separate `da_helpers.py` file.

Further note that this is work in progress rather than a finished package.

### Tabled functions

| | Python | R |
|---|---|---|
| List zip archive contents | `itemise_archive` | `itemise_archive` |
| Open or extract a file from an archive | `extract_file`, `copy_archived_file` | `extract_file`, `copy_archived_file` |
| Read the rtf data dictionary as text | `read_data_dictionary` | `read_data_dictionary` |
| Variable -> (column position, label) | `variable_dictionary` | `variable_dictionary` |
| Variable -> {code: label} | `code_dictionary` | `code_dictionary` |
| Read a `.tab` file with cleaned names | `read_tab_pd`, `read_tab_pl` | `read_tab` |

## See also

* [Labour Force Survey user guidance](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/methodologies/labourforcesurveyuserguidance)
