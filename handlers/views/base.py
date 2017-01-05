from tornado.concurrent import return_future
from tornado import escape

from collections import OrderedDict

import numpy as np
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import mpld3


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
            columns[column] = self._get_column_description(column)
        callback({'columns': columns})

    @return_future
    def plot_columns(self, callback=None):
        plots = OrderedDict()
        for column in self.data.columns:
            plots[column] = self._plot_column(column)
        callback({'plots': plots})

    def _get_column_description(self, column):
        desc = escape.json_decode(
            self.data[column].describe(include='all').to_json()
        )
        dtype = self.data[column].dtype
        desc.update({
            'dtype': str(dtype),
            'num_undefined': int(
                self.data.shape[0] - self.data[column].count()
            )
        })

        if (dtype == np.float64 or dtype == np.int64):  # numeric dtype
            desc.update({
                'unique': len(self.data[column].unique()),
                'median': desc.pop('50%')
            })
        else:  # object, datetime e.t.c
            pass
        return desc

    def _plot_column(self, column):
        plot = None
        dtype = self.data[column].dtype
        if (dtype == np.float64 or dtype == np.int64):  # numeric dtype
            plot = self.build_box_plot(self.data[column])
        else:  # object, datetime e.t.c
            pass
        return plot

    def build_box_plot(self, data):
        fig, ax = plt.subplots()
        data.plot(kind='box', ax=ax)
        return escape.json_encode(mpld3.fig_to_dict(fig))

    def build_barh_plot(self, data):
        pass
