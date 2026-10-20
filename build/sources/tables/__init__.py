"""One module per track, each exposing DATA: {item-text-substring: (learn, practise, evidence)}.

Split per track because these are written by different research passes at
different times, and a bad merge in one track must not be able to corrupt
another. apply_table.py discovers them by filename.
"""
