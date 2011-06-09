from model.network import Network
from model.unix_route_table import UnixRouteTableConverter

net = Network('./src/model/small_topology.net')
route_tables = net.get_route_tables()

unix = UnixRouteTableConverter(route_tables, './scripts/')
unix.execute()