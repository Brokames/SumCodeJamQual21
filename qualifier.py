
from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    # Setup
    format_char = '^' if centered else '<'
    colsWidth = [0] * (len(rows[0]))
    # Column Width and dealing with None
    if labels is not None:
        labels = ["None" if label is None else label for label in labels]
        for i, label in enumerate(labels):
            if len(str(label)) > colsWidth[i]:
                colsWidth[i] = len(str(label))
    rows = [["None" if col is None else col for col in row] for row in rows]
    for row in rows:
        for i, col in enumerate(row):
            if len(str(col)) > colsWidth[i]:
                colsWidth[i] = len(str(col))
    # Make top of table
    table = fillBorder(colsWidth, '┌', '─', '┬', '┐\n')
    # Deal with labels
    if labels is not None:
        table += fillInfo(labels, colsWidth, '│', '│', '│\n', format_char)
        table += fillBorder(colsWidth, '├', '─', '┼', '┤\n')
    # Deal with fill
    for row in rows:
        table += fillInfo(row, colsWidth, '│', '│', '│\n', format_char)
    # Make bottom of table
    table += fillBorder(colsWidth, '└', '─', '┴', '┘')
    return table


def fillBorder(columnWidth: List[int], startChar: chr, fillChar: chr, swapChar: chr, endChar: str) -> str:
    output = startChar
    for i, w in enumerate(columnWidth):
        output += fillChar * (w + 2)
        if i != len(columnWidth) - 1:
            output += swapChar
    output += endChar
    return output


def fillInfo(data: List[Any], columnWidth: List[int], startChar: chr, swapChar: chr, endChar: str, formatChar: chr) -> str:
    output = startChar
    for i, w in enumerate(columnWidth):
        output += ' ' + ("{:" + formatChar + str(w) + "}").format(str(data[i])) + ' '
        if i != len(columnWidth) - 1:
            output += swapChar
    output += endChar
    return output
