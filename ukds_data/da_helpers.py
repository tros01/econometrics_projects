# ============================================================
# da_helpers.py — Generic data analysis utilities
# rev2026-10-30
# ============================================================
#
# crawl_folder:    List all files in a folder and its subfolders
# extract_file:    Open a file inside a zip archive
# itemise_archive: List the files in a zip archive
# read_rtf:        Convert an RTF file handle to plain text
# read_tab_pd:     Read a tab-delimited file into pandas, with clean column names
# read_tab_pl:     Read a tab-delimited file into polars, with clean column names
#
# ============================================================
# Imports
import zipfile
import os.path

from striprtf.striprtf import rtf_to_text
# ============================================================

def crawl_folder(folder_path):
    """
    Returns a list of files in a folder and subfolders.
    libraries:          import os
    input:              folder_paths: str
    output:             list
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError("The folder path does not exist.")

    file_paths = []
    for path, directories, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(path, file))
    return(file_paths)

def extract_file(zip_path, file_name):
    """
    Opens a file inside a zip archive.
    libraries:          import zipfile
    input:              zip_path: str | file-like, file_name: str
    output:             zipfile.ZipExtFile
    """
    with zipfile.ZipFile(zip_path, "r") as archive:
        return archive.open(file_name)

def itemise_archive(zip_path):
    """
    Returns a list of files in a zip archive.
    libraries:          import zipfile
    input:              zip_path: str | file-like
    output:             list
    """
    with zipfile.ZipFile(zip_path, "r") as archive:
        return archive.namelist()

def read_rtf(raw_rtf):
    """
    Converts an rtf file handle to plain text.
    libraries:          from striprtf.striprtf import rtf_to_text
    input:              raw_rtf: binary file-like
    output:             str
    """
    return rtf_to_text(raw_rtf.read().decode("cp1252"))

def read_tab_pd(file, header=True, nrows=None, cols=None):
    """
    Reads a tab-delimited file into a pandas DataFrame with cleaned column names.
    libraries:          import pandas as pd, from skimpy import clean_columns
    input:              file: str | file-like, header: bool, nrows: int | None, cols: list | None
    output:             pd.DataFrame
    """
    import pandas as pd
    from skimpy import clean_columns
    df = pd.read_csv(
        file, 
        sep="\t", 
        header=0 if header else None,
        nrows=nrows, 
        usecols=cols
    )
    return clean_columns(df)

def read_tab_pl(file, header=True, nrows=None, cols=None):
    """
    Reads a tab-delimited file into a polars DataFrame with cleaned column names.
    libraries:          import polars as pl, from skimpy import clean_columns
    input:              file: str | file-like, header: bool, nrows: int | None, cols: list | None
    output:             pl.DataFrame
    """
    import polars as pl
    from skimpy import clean_columns
    df = pl.read_csv(
        file, 
        separator="\t", 
        has_header=header,
        n_rows=nrows, 
        columns=cols
    )
    return clean_columns(df)
