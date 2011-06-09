import ConfigParser

def build_topology_file(path):
	'''
		Crea una topologia.
	'''
	file = open(path,'w')
	parser = ConfigParser.ConfigParser() 

	parser.add_section('H102')
	parser.set('H102', 'eth0:0', '10.31.6.1/24')
	parser.set('H102', 'eth0:1', '10.54.5.65/27')

	parser.add_section('H104')
	parser.set('H104', 'eth0:0', '10.31.6.2/24')
	parser.set('H104', 'eth0:1', '10.54.5.66/27')
	
	parser.add_section('H106')
	parser.set('H106', 'eth0:0', '10.31.6.3/24')
	parser.set('H106', 'eth0:1', '192.168.8.2/24')
	parser.set('H106', 'eth0:2', '10.11.6.193/26')
			
	parser.add_section('H1')
	parser.set('H1', 'eth0:0', '10.54.5.67/27') 
	parser.set('H1', 'eth0:1', '172.23.5.197/30') 
	parser.set('H1', 'eth0:2', '172.23.5.201/30') 

	parser.add_section('H108')
	parser.set('H108', 'eth0:0', '10.54.5.68/27')
	parser.set('H108', 'eth0:1', '10.54.5.41/30')

	parser.add_section('H116')
	parser.set('H116', 'eth0:0', '10.54.5.42/30')
	parser.set('H116', 'eth0:1', '10.54.5.131/28')

	parser.add_section('H114')
	parser.set('H114', 'eth0:0', '10.54.5.129/28')
	parser.set('H114', 'eth0:1', '10.54.9.132/25')
	parser.set('H114', 'eth0:2', '10.54.5.98/27')
	parser.set('H114', 'eth0:3', '10.54.5.45/30')

	parser.add_section('H111')
	parser.set('H111', 'eth0:0', '10.54.9.130/25')
	parser.set('H111', 'eth0:1', '172.23.5.193/30')
	parser.set('H111', 'eth0:2', '172.23.5.198/30')

	parser.add_section('H113')
	parser.set('H113', 'eth0:0', '10.54.9.131/25')
	parser.set('H113', 'eth0:1', '10.54.5.97/27')
	parser.set('H113', 'eth0:2', '172.23.5.194/30')
	parser.set('H113', 'eth0:3', '172.23.5.202/30')

	parser.add_section('H117')
	parser.set('H117', 'eth0:0', '10.54.5.99/27')
	parser.set('H117', 'eth0:1', '130.63.5.1/30')

	parser.add_section('H121')
	parser.set('H121', 'eth0:0', '10.54.5.1/27')
	parser.set('H121', 'eth0:1', '130.63.5.2/30')

	parser.add_section('H122')
	parser.set('H122', 'eth0:0', '10.54.17.1/24')
	parser.set('H122', 'eth0:1', '10.54.5.46/30')
	parser.set('H122', 'eth0:2', '10.54.5.2/27')
	parser.set('H122', 'eth0:3', '10.54.5.161/30')
	parser.set('H122', 'eth0:4', '10.54.5.177/30')
	parser.set('H122', 'eth0:5', '10.54.5.181/30')
	parser.set('H122', 'eth0:6', '10.54.5.185/30')
	parser.set('H122', 'eth0:7', '10.54.5.189/30')
	parser.set('H122', 'eth0:8', '10.54.5.193/30')
	parser.set('H122', 'eth0:9', '10.54.5.197/30')
	
			
	parser.write(file)
	
	file.close()

# Builds the topology.
build_topology_file("full_topology.net")
