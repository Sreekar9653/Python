# Program for counting the number of characters

a = input( "Enter word, enter stop if done " )		# user input
while( a != "stop" ):					# stops when user enters stop
    d = dict()						# empty dictionary
    for i in range( len(a) ):				
        if( a[i] not in a[:i] ):			# Checking if character already counted
            d[a[i]] = a.count(a[i])			# inserting { character:count } pair
    print(d)
    a=input( "Enter word, enter stop if done " )	# infinite loop until a = "stop"
    
