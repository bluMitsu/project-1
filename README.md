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
    network=[]
    connected= string_input.find('is connected to')
    if connected == -1:
        return network
    else:
        network.append([ string_input[: string_input.find(' ')] ])
        
        dic={'connections':[], 'games':[]}
        first_dot=string_input.find('.')
        connected= string_input.find('is connected to')
        plays= string_input.find('likes to play')
        
        sub_string= string_input[ connected + len('is connected to')+1 : first_dot]
        fill_dic(dic,'connections',sub_string)
        
        sub_string= string_input[ plays + len('likes to play')+1 : string_input.find('.',first_dot+1) ]
        fill_dic(dic,'games',sub_string)
            
        
        network[ len(network)-1 ].append(dic)
        
        new_string= string_input[string_input.find('.', first_dot+1 ) + 1:]
        return network + create_data_structure(new_string)

print create_data_structure(example_input)
