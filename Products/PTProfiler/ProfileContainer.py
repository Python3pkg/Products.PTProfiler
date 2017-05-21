"""The container for the profiler
"""


class ProfileContainer:
    """The container (nested dict) for the profiling result
    """
    def __init__(self):
        self._templates = {}

    def expr_hit(self, templatename, expr, time):
        """Add the data of a hit to the dict
        """
        if templatename not in self._templates:
            self._templates[templatename] = {}

        template = self._templates[templatename]

        if expr not in template:
            template[expr] = {}
            template[expr]['time'] = time
            template[expr]['hits'] = 1
        else:
            template[expr]['time'] += time
            template[expr]['hits'] += 1

    def pt_hit(self, templatename, time):
        if templatename not in self._templates:
            self._templates[templatename] = {}

        template = self._templates[templatename]

        key = 'total'
        if key not in template:
            template[key] = {}
            template[key]['time'] = time
            template[key]['hits'] = 1
        else:
            template[key]['time'] += time
            template[key]['hits'] += 1

    def clear(self):
        self._templates = {}

# create a global instance of the container
profile_container = ProfileContainer()

