# left join

1. Write a function that LEFT JOINs two hashmaps into a single data structure.
1. The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
1. The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
1. Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
1. LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
1. The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic.
1. Avoid utilizing any of the library methods available to your language.

![left_join_hash_tables](../../assets/left-join.png)
