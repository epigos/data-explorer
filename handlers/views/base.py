from tornado.concurrent import return_future
from tornado import escape

from collections import OrderedDict

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt, mpld3

__all__ = ['BaseView', ]


class BaseView(object):

    def __init__(self, data, config):
        self.data = data
        self.config = config

    @return_future
    def get_data_summary(self, callback=None):
        rows, columns = self.data.shape
        results = {
            'summary': {
                'type': 'DataFrame',
                'rows': rows,
                'cols': columns,
            }
        }
        callback(results)

    @return_future
    def describe_columns(self, callback=None):
        columns = OrderedDict()
        for column in self.data.columns:
            columns[column] = escape.json_decode(
                self.data[column].describe().to_json()
            )
        callback({'columns': columns})

    def build_plot(self, data):
        fig, ax = plt.subplots()
        data.plot(ax=ax)
        return escape.json_encode(mpld3.fig_to_dict(fig))
