# project-1
this is a practice project done for end of the course Intro To CS (on Udacity)

def fill_dic(dic,key,string):
    if string.find(',') == -1:
        return dic[key].append(string)
    else:
        comma= string.find(',')
        dic[key].append(string[ : comma ])
        string= string[comma+2 :]        
        fill_dic(dic,key,string)

def create_data_structure(string_input):
    network={}
    connected= string_input.find('is connected to')
    while string_input.find('is connected to') != -1:
        dic={'connections':[], 'games':[]}
        first_dot=string_input.find('.')
        connected= string_input.find('is connected to')
        plays= string_input.find('likes to play')
        
        sub_string= string_input[ connected + len('is connected to')+1 : first_dot]
        fill_dic(dic,'connections',sub_string)
        
        sub_string= string_input[ plays + len('likes to play')+1 : string_input.find('.',first_dot+1) ]
        fill_dic(dic,'games',sub_string)
            
        network[string_input[: string_input.find(' ')]]= dic
        string_input= string_input[string_input.find('.', first_dot+1 ) + 1:]
    return network

print create_data_structure(example_input)

def get_connections(network, user):
    if user in network:    
        return network[user]['connections']
	return None
   
def get_games_liked(network,user):
     if user in network:    
        return network[user]['games']
	return None
    
def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    elif user_B in get_connections(network, user_A):
        print "network unchanged"
    else:
	    get_connections(network, user_A).append(user_B)
    return network
 
 def add_new_user(network, user, games):
    if user in network:
        print "network unchanged"
    else:
        network[user]={"connections":[],"games": games}
    return network
    
def get_secondary_connections(network, user):
    if user not in network:
        return None
    
    sec_connections= []
    for connection in get_connections(network, user):
        for second in get_connections(network,connection):
            if second not in sec_connections: 
                sec_connections += [second] 
    return sec_connections
    
def count_common_connections(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
        
    common=0
    for user in get_connections(network, user_A):
        if user in get_connections(network, user_B):
            common += 1
    return common
    
 
