# coding: utf-8

from pathlib import Path
import pickle
import pandas as pd
import numpy as np


def read_pickled_pages(fn):
    pickle_files = Path('.').glob(fn)
    statuses = []
    for page_fn in pickle_files:
        with open(page_fn, 'rb') as f:
            statuses.extend(pickle.load(f))
    return statuses


def flatten_dict(nested_json, exclude=['']):
    """Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
            exclude: Keys to exclude from output.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name='', exclude=exclude):
        if type(x) is dict:
            for a in x:
                if a not in exclude: flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out

def statuses_to_pandas(statuses):
    data = []
    for status in statuses:
        data.append(flatten_dict(status._json))
    return pd.DataFrame(data)


def keep_only_user_id_fields(df):
    def is_user_id_column(c):
        return (('user_id' in c.lower() 
                 or ('user_mentions' in c.lower() and 'id' in c.lower()))
                 and not 'str' in c.lower())
    user_columns = sorted([c for c in df.columns if is_user_id_column(c)], key=len)
    df_nx = df[user_columns] 
    return df_nx


def user_df_to_graph(df_nx):

    graph = set()
    for index, row in df_nx.iterrows():
        user_id = row[0]
        assert(not np.isnan(user_id))
        for other_id in row[1:]:
            try:
                if other_id is not None and not np.isnan(other_id):
                    graph.add((int(user_id), int(other_id)))
            except TypeError:
                pass


    df_graph = pd.DataFrame(graph, columns=['src', 'dest'])
    return df_graph
