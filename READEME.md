# Lab: Cryptography

### Overview

Today we’ll be tackling a cryptographic classic - the Caesar Cipher.

Your job will be to devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.

But don’t stop there! You’ll also need to devise a way to decipher the encrypted message event when you do NOT have the key!

### Feature Tasks and Requirements
1. Create an encrypt function that takes in a plain text phrase and a numeric shift.
the phrase will then be shifted that many letters.
E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’

2. Shifts that exceed 26 should wrap around
E.g. encrypt(‘abc’,27) would return ‘bcd’

3. Shifts that push a letter out or range should wrap around
E.g. encrypt(‘zzz’,1) would return ‘aaa’

4. Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

5. Create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

6. Devise a method for the computer to determine if code was broken with minimal human guidance.

### Implementation Notes
In order to accomplish a certain task you’ll need access to a corpus of English words.
A search on something like python list of english words should get you going.

### User Acceptance Tests
The application must…

1. encrypt a string with a given shift
1. decrypt a previously encrypted string with the same shift
1. encryption should handle upper and lower case letters
1. encryption should allow non-alpha characters but ignore them, including white space
1. decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
1. refer to supplied unit tests.

### Stretch Goals
1. Research the Vigenère cipher
1. Find some examples of ROT13 encrypted punchlines, spoilers, etc.
1. Break the code for a message written in language other than English.

### Configuration
Use poetry to create caesar-cipher project.

```$ poetry new caesar-cipher```
Use the folder created by Poetry as the root of your project’s git repository.
