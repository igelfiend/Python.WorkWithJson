# -*- coding: utf-8 -*-
import json
import requests

def isTaskUnique(srcData, checkObj):
    # In source list at unique case must be 1 element found
    # In other cases, element not unique
    counter = 0
    for element in srcData:
        if element[ "title" ] == checkObj["title"]:
            counter += 1
        if counter > 1:
            return False
    return True

def main():
    # Reading data from site
    response = requests.get( "https://jsonplaceholder.typicode.com/todos" )
    data = json.loads( response.text )

    # Saving response to file
    with open( "response.txt", "w" ) as f:
        json.dump( data, f, indent=4 )

	# Making dict with data for each user, contains unique tasks count and complete tasks count
    users = {}

    for record in data:
        # If no user found, make blank record for him
        if record[ "userId" ] not in users.keys():
            users[ record[ "userId" ] ] = {}
            users[ record[ "userId" ] ][ "complete_tasks" ] = 0
            users[ record[ "userId" ] ][ "unique_tasks"   ] = 0

        # Checking unique condition
        if isTaskUnique( data, record ):
            users[ record[ "userId" ] ][ "unique_tasks" ] += 1
            # Checking completing condition
            if record[ "completed" ] == True:
                users[ record[ "userId" ] ][ "complete_tasks" ] += 1

    for user in users:
        print( "\n" )
        print( "Current user:   ", user )
        print( "Unique tasks:   ", users[ user ][ "unique_tasks" ] )
        print( "Complete tasts: ", users[ user ][ "complete_tasks" ] )

    print( "\nUnique users count: ", len( users.keys() ) )

if __name__ == "__main__":
    main()
