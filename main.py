#
#
#
#

class PickAUniqueName(Exception):
    """
    A custom error class for when a route is created, but the name is already in use.
    """

    pass

class TransitStopNode:
    """
    TODO
    """
    def __init__(self, route_name, stop_name, stop_order):
        self._stop_name = stop_name
        self._stop_order = {route_name: stop_order}
        self._stop_direction = {}
        self._location = {"lat": None, "long": None, "address": None}
        self._ridership = None
        self._amenities = None
        self._routes = []
        self._layover = False
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

    def set_layover(self, bool_value):
        """
        TODO
        """

        self._layover = bool_value

    def add_route(self, route_obj):
        """
        TODO
        """

        self._routes.append(route_obj)

    def get_routes(self):
        """
        TODO
        """

        return self._routes

    def get_lat_location(self):
        """
        TODO
        """

        return self._location["lat"]

    def get_long_location(self):
        """
        TODO
        """

        return self._location["long"]

    def get_address_location(self):
        """
        TODO
        """

        return self._location["address"]

    def set_lat_location(self, lat_float):
        """
        TODO
        """

        self._location["lat"] = lat_float

    def set_long_location(self, long_float):
        """
        TODO
        """

        self._location["long"] = long_float

    def set_address_location(self, address_string):
        """
        TODO
        """

        self._location["address"] = address_string



class TransitSystem:
    """
    TODO
    """
    def __init__(self, system_name):
        self._route_dictionary = {}  # Route name as key, Route object as value
        self._system_name = system_name



    def create_route(self, route_name, stop_name_list):
        """
        TODO
        """
        if route_name not in self._route_dictionary.keys():
            return

        else:
            raise PickAUniqueName("Sorry! "+str(route_name)+" is already in use!  Please pick a unique route name.")

        #return


class TransitRoute:
    """
    TODO
    """
    def __init__(self, route_name, circulator, stop_names_list):
        self._route_name = route_name
        self._circulator = circulator
        self._stop_names = stop_names_list
        self._stop_dictionary = {}
        self._first_stop = None

    def create_stops(self, route_name, stop_name_list):
        """
        TODO
        """

        self._first_stop = TransitStopNode(route_name, stop_name=stop_name_list[0], stop_order=0)
        current = self._first_stop
        self._X_dictionary[current.get_stop_name()] = current

        for indx in range(1,len(stop_name_list)):
            current.next_stop = TransitStopNode(route_name, stop_name=stop_name_list[0], stop_order=indx)
            current = current.get_next_stop()
            self._X_dictionary[current.get_stop_name()] = current

        current.next_stop = self._first_stop

    def get_route_name(self):
        """
        TODO
        """

        return self._route_name

    def get_circulator(self):
        """
        TODO
        """

        return self._circulator

    def set_circulator(self, bool_value):
        """
        TODO
        """

        self._circulator = bool_value