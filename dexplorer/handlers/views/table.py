from collections import namedtuple

_TableView = namedtuple('_TableView', ('data', ))


class Table(_TableView):

    def paginate(self, start=0, limit=100):
        """
            Paginate dataframe
            Args:
                start: int, default 0
                limit: int, default 100
            Returns:
                json
        """
        return self.data.iloc[start:limit].to_json(orient='split')
