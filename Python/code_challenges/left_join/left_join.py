def left_join_hash(left_hash, right_hash):
    # empty that will hold final merged lists
    joined_hash = []

    # Loop through the left_hash table
    for key in left_hash:
        # empty list that will reset to empty with each loop
        row = []
        # append the key and the value from left_hash
        row.append(key)
        row.append(left_hash[key])

        # for every key in left_hash lets check the right_hash for the same key
        try:
            # if found lets append just the value from right_hash
            if right_hash[key]:
                row.append(right_hash[key])
        # if not present just append None to the current key
        except:
            row.append(None)
        # add the current key and what ever values present to the new
        joined_hash.append(row) # adds row results to the joined_hash list

    # return the joined_hash list with both left and right lists merged
    return joined_hash
