import requests
import pandas as pd
import numpy as np
import json


class Query(object):
    def __init__(self, server, targets=[], start='-1h', end='now'):
        self.server = server
        self.targets = targets
        self.start = start
        self.end = end

    def target(self, target):
        return Query(
            self.server,
            targets=self.targets + [target],
            start=self.start,
            end=self.end
        )

    def pfrom(self, start):
        return Query(
            self.server,
            targets=self.targets,
            start=start,
            end=self.end
        )

    def puntil(self, end):
        return Query(
            self.server,
            targets=self.targets,
            start=self.start,
            end=end
        )

    def _url(self):
        params = []
        params += ["target=%s" % target for target in self.targets]
        params += ["from=%s" % self.start, "until=%s" % self.end]
        url = self.server + '/render?format=json&' + '&'.join(params)
        return url

    def execute(self):
        py_data = json.loads(requests.get(self._url()).text)
        np_data = [(series['target'], np.array(series['datapoints'])) for series in py_data]
        series = [pd.DataFrame(series[:, 0], index=series[:, 1], columns=[target]) for target, series in np_data if series.any()]
        if len(series) > 0:
            return pd.concat(series, axis=1, join='inner')
        else:
            return None
