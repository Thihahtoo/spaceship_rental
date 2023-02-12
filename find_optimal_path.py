def build_neighbour(contract):
    '''
        Create next hop for each contract.  
        
        Parameters
        ----------
        contracts : list
            Should be a list of dicts with 4 mandatory keys (name str, start int, duration int and price int)
            eg: [
                    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
                    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
                    {"name": "Contract3", "start": 5, "duration": 9, "price": 8}
                ]
        
        Returns
        -------
        A set of tuples with neighbour including cost for each node
            eg: {
                    ('Contract1:10', 'Contract3:8')
                    ('Contract2:14', None)
                }
        
        Raises
        ------
        Exception:
            Missing required keys in provided json body.
    '''
    neigh_set = set({})
    for c in contract:
        if set(c.keys()) == {'name','start','duration','price'}:
            neig = ()
            end = c['start'] + c['duration']
            for j in contract:
                if j['start'] >= end:
                    neig = (f"{c['name']}:{c['price']}", f"{j['name']}:{j['price']}")
                    neigh_set.add(neig)
                    
            if not neig:
                neigh_set.add((f"{c['name']}:{c['price']}", None))
        else:
            raise Exception("Missing required keys in provided json body.")
    return neigh_set


def calculate_total_profit(path_tuple):
    '''
        Calculate total profit for path.  
        
        Parameters
        ----------
        contracts : tuple
            Tuple with contract and price separated by ':'
            eg: ('c1:10', 'c2:1', 'c5:2', None)
        
        Returns
        -------
        path, profit: tuple, integer
            A tuple of contract path and total profit.
    '''
    path = []
    profit = 0
    for ele in path_tuple:
        if ele is not None:
            c, p = ele.split(':')
            path.append(c)
            profit = profit + int(p)
    return (tuple(path), profit)


def find_path(contract):
    '''
        Find the optimal path with maximum profit.  
        
        Parameters
        ----------
        contracts : list
            Should be a list of dicts with 4 mandatory keys (name str, start int, duration int and price int)
            eg: [
                    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
                    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
                    {"name": "Contract3", "start": 5, "duration": 9, "price": 8}
                ]
        
        Returns
        -------
        best_path: list
            A list of contract names maximizing the profit.
        max_price: int
            Maximum total profit
    '''
    main_dict = {}
    neigh_set = build_neighbour(contract)
    tmp_set = neigh_set
    holder_set = neigh_set

    while holder_set:
        holder_set = set({})
        for tup1 in tmp_set:
            path, profit = calculate_total_profit(tup1)
            main_dict[path] = profit
            
            for tup2 in neigh_set:
                if tup1[-1] == tup2[0]:
                    holder_set.add(tup1 + (tup2[-1],))
        
        tmp_set = holder_set
    
    best_path = max(main_dict, key=main_dict.get)
    max_profit = main_dict[best_path]
    return list(best_path), max_profit
