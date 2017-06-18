while True: # Main loop
    # Get sensors statuses
	result = [i.is_ok() for i in sensors] 
    if False in result:
        print('Not OK', end='\r')
        # Take an action
		controller.lower_priority() 
    else:
        print('Everything is OK', end='\r')
    # Time interval between cicles
	sleep(_options.period) 
