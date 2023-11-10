Unsplice
---------

Given a string, strip all occurrences of consecutively occurring
backslash and newline characters.
For example, assuming that:

"\\" represents '\' and
"\n" represents '\n'

Examples:
"ab\\\ncd\\\nef" --> "abcdef" (two stripped out)
"abc\\\ndef" --> "abcdef" (one stripped out)
"abc\n\\def" --> unchanged (wrong order)
"abc\\def" --> unchanged (no \n)
"abc\ndef" --> unchanged (no \)
"abcdef" --> unchanged
