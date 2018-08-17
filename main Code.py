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
    
def find_path_to_friend(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return None
    return friends (network, user_A, user_B, friend = None)        
    
def friends (network, user_A, user_B, friend = None):    
    if friend == None:
        friend = []
    friend = friend + [user_A]
    
    if user_A == user_B:
        return friend

    for node in network[user_A]['connections']:
        if node not in friend :
            next_friend = friends(network,node,user_B,friend)
            if next_friend:
                return next_friend 
    return None

#Test example:

example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


net = create_data_structure(example_input)

print net
print get_connections(net, "Debra")
print get_connections(net, "Mercedes")
print get_games_liked(net, "John")
print add_connection(net, "John", "Freda")
print add_new_user(net, "Debra", [])
print get_secondary_connections(net, "Mercedes")
print count_common_connections(net, "Ollie", "John")
print find_path_to_friend(net, "John","Ollie")
