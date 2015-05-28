"""
Several useful functions for doing things with tuples that I'm writing
"""

def tuple_value_change_with_kwargs( a_tuple=(2, 3, 4, 5), an_int=6 ):

    print a_tuple, an_int
    print a_tuple[1:]
    print a_tuple * 2
    print (an_int,) + a_tuple[1:]
    new_tuple= (an_int,) + a_tuple[1:]
    return new_tuple

def find_tup_lengths(tuples) :
    """
    Returns the length of tuples that have ben input.
    e.g.
    Start with: find_tup_lengths( [(1, 2, 3), (5, 6), (1, 10, 100, 1000)])
    find_tup_lengths( [(1, 2, 3), (5, 6), (1, 10, 100, 1000)])
    >> [3, 2, 4]
    """
    print tuples
    returndef find_tup_lengths(tuples) :
    """                                                                         
    Returns the length of tuples that have ben input.                           
    e.g.                                                                        
    Start with: find_tup_lengths( [(1, 2, 3), (5, 6), (1, 10, 100, 1000)])      
    find_tup_lengths( [(1, 2, 3), (5, 6), (1, 10, 100, 1000)])                  
    >> [3, 2, 4]                                                                
    """
    print tuples
    
    def find_tup_lengths(tuples) :
    """                                                                         
    Returns the length of tuples that have ben input.                           
    e.g.                                                                        
    Start with: find_tup_lengths( [(1, 2, 3), (5, 6), (1, 10, 100, 1000)])      
    find_tup_lengths( [(1, 2, 3), (5, 6), (1, 10, 100, 1000)])                  
    >> [3, 2, 4]                                                                
    """
    print tuples
    
    list_tup = []
    print type(tuples)
    
    for tup in tuples:
        print tup
        list_tup.append(len(tup))
        print (len(tup))
    return list_tup
