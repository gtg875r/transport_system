#
#
#
#


class TransitStopNode:
    """
    TODO
    """
    def __init__(self, stop_name, layover=False):
        self._stop_name = stop_name
        self._stop_order = {}
        self._stop_direction = {}
        self._location = {"lat": None, "long": None, "address": None}
        self._ridership = None
        self._amenities = None
        self._routes = []
        self._layover = layover
        self.next_stop = None

    def __repr__(self):
        """TODO"""
        return "TransitStopNode (Stop Name: " + str(self._stop_name) + ")"

    def __str__(self):
        return "TransitStopNode (Stop Name: " + str(self._stop_name) + ")"

    def get_stop_name(self):
        """
        TODO
        """

        return self._stop_name

    def get_stop_order(self, route):
        """
        TODO
        """

        return self._stop_order[route]

    def get_stop_direction(self, route):
        """
        TODO
        """

        return self._stop_direction[route]

    def get_next_stop(self):
        """
        TODO
        """

        return self.next_stop

    def get_layover(self):
        """
        TODO
        """

        return self._layover

