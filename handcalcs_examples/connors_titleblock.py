"""
Contains helper functions for performing calculations in Jupyter Notebook.
Use dir(rjc.jupyter) for a directory of the functions.

Connor Ferster, cferster@rjc.ca 2021
"""
from IPython.display import display, Markdown
import datetime

def title_block(proj_name = "", proj_id = "", designer = "", _test=False, **kwargs) -> None:
    """
    Returns None. Displays a simple title block for engineering notes created in Jupyter.
    
    '_test' argument is used for internal testing: returns the markdown as a string instead
    of displaying in Jupyter.
    """
    todays_date = datetime.datetime.now().strftime("%Y-%m-%d")
    md = (
        f"**Project:** {proj_name}<br>\n"
        f"**Project ID:** {proj_id}<br>\n"
        f"**Designer:** {designer}<br>\n"
        f"**Date:** {todays_date}<br>\n"
    )
    extra_md = ""
    for kw, arg in kwargs.items():
        extra_md += f"**{kw}:** {arg}<br>\n"
    display(Markdown(md + extra_md))
    if _test:
        return md