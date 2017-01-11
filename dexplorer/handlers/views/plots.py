from collections import namedtuple
from io import StringIO

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt  # NOQA
import mpld3  # NOQA

from .utils import smart_truncate  # NOQA

_BasePlot = namedtuple('BasePlot', ('data', ))


class BasePlot(_BasePlot):

    @classmethod
    def destory_fig(cls, fig=None):
        if fig:
            fig.clear()
            plt.close(fig)


class SummaryPlot(BasePlot):
    """docstring for Summary Plot"""

    def generate_boxplot(self):
        color = dict(boxes='#FAA43A', whiskers='DarkOrange',
                     medians='DarkBlue', caps='Gray')

        fig, ax = plt.subplots()
        self.data.plot.box(
            ax=ax, color=color,
            boxprops=dict(linewidth=4), whiskerprops=dict(linewidth=2),
            medianprops=dict(linewidth=4), capprops=dict(linewidth=2),
            showfliers=False, figsize=(8, 4), showmeans=True, meanline=True
        )
        # Add a horizontal grid to the plot, but make it very light in color
        # so we can use it for reading data values but not be distracting
        ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                      alpha=0.5)
        # Hide these grid behind plot objects
        ax.set_axisbelow(True)
        # Fit plot in canvas
        fig.tight_layout()
        return self._build_mpld3_plot(fig)

    def generate_barh(self):
        fig, ax = plt.subplots()
        values = self.data.value_counts()[:10]
        values.sort_values(ascending=True, inplace=True)
        values.plot.barh(ax=ax, figsize=(8, 4), color='#FAA43A', alpha=0.5)

        # Truncate long tick labels
        labels = [smart_truncate(l.get_text(), 30)
                  for l in ax.get_yticklabels()]
        ax.set_yticklabels(labels)

        # Add a horizontal grid to the plot, but make it very light in color
        # so we can use it for reading data values but not be distracting
        ax.xaxis.grid(True, linestyle='-', which='major', color='lightgrey',
                      alpha=0.5)
        # Hide these grid behind plot objects
        ax.set_axisbelow(True)
        # Fit plot in canvas
        fig.tight_layout()
        # build matplotlib d3 plot
        return self._build_mpld3_plot(fig)

    def _build_mpld3_plot(self, fig):
        # Fit plot in canvas
        fig.tight_layout()
        io = StringIO()
        mpld3.save_json(fig, io)
        return (io.getvalue(), fig)
