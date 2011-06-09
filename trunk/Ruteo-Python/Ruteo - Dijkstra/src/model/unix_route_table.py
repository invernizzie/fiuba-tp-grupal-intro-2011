class UnixRouteTableConverter(object):
    
    def __init__(self, route_tables, path):
        '''
            route_tables: contiene las tablas de ruteo calculadas por la clase 'network'
            path: indica el directorio destino donde se ubicaran los archivos de salida.
        '''
        self.route_tables = route_tables
        self.path = path
        
    def execute(self):
        for router in self.route_tables.keys():
            table = self.route_tables[router]
                        
            script = open(self.path + router.id + '.sh', 'w')
            script.write('#! /bin/bash\n\n')
            
            script.write('echo "1" > /proc/sys/net/ipv4/ip_forward\n\n')
            
            # Obtenemos el nombre de la interfaz a utilizar.        
            script.write('INTERFACE=$(ifconfig -a | grep -o eth[0-9] | tail -n 1)\n\n')
            
            # Limpiamos la configuracion anterior. 
            script.write('OTHER_INTS=$(ifconfig -a | grep -o eth[0-9]:[0-9])\n\n')
            script.write('for INT in $OTHER_INTS\n')
            script.write('do\n')
            script.write('ifconfig $INT down\n')
            script.write('done\n\n')
            
            script.write('ifconfig $INTERFACE up\n\n')
            
            count = 0        
            for interface in router.interfaces:
                script.write('ifconfig $INTERFACE:' + str(count) + ' ' + interface.get_ip_str())
                script.write('\n')
                count += 1
                
            script.write('\n')
            
            # Liempiamos las tablas de ruteo.
            for entry in table:
                command_line = 'route add -net ' + entry[0] + ' netmask ' \
                                + entry[1] + ' gw ' + entry[3] + '\n' 
                script.write(command_line)
                
            script.close()