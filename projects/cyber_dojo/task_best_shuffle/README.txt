Best Shuffle
------------

Shuffle the characters of a string in such a way that as many
of the character values are in a different position as possible.

Display the result as follows:
  original string, shuffled string, (score)

The score gives the number of positions whose character value did not change.

Example
  tree, eert, (0)

Test cases
  abracadabra
  seesaw
  elk
  grrrrrr
  up
  a


[Source https://rosettacode.org/wiki/Best_shuffle]


......
Additional hints:

Test cases with possible solutions when we sort the permutations,
so the tests will always pass when the code is correct:
  tree, eert, (0)
  abracadabra, baabacadrar, (0)
  seesaw, assewe, (0)
  elk, kel, (0)
  grrrrrr, rgrrrrr, (5)
  up, pu, (0)
  a, a, (1)

Additional Tests
  mediate, adeeimt, (0)
  immediately, adeielimmyt, (0)
  thegreatestbearofalltime, harttgmerbaeleofleeiastt, (0)
  you must be kidding; right; buddy?, ui?byiyrd tgt mue;d uhd;oi gkd bns, (0)
