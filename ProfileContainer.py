"""The container for the profiler
"""

class ProfileContainer:
    """The container (nested dict) for the profiling result
    """
    def __init__(self):
        self._templates = {}

    def hit(self, templatename, expr, time):
        """Add the data of a hit to the dict
        """
        if not self._templates.has_key(templatename):
            self._templates[templatename] = {}

        template = self._templates[templatename]

        if not template.has_key(expr):
            template[expr] = {}
            template[expr]['time'] = time
            template[expr]['hits'] = 1
        else:
            template[expr]['time'] += time
            template[expr]['hits'] += 1

# create a global instance of the container
profile_container = ProfileContainer()

