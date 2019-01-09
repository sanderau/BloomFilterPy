** IMPORTANT **
 == I am using the bitarray library for python! Theoretically pip should be able to handle with the command 'pip install bitarray'
 == However if that doesn't, like it didn't for me, you will have to use the command 'sudo apt-get install python-bitarray'
 == I am sorry in advance computers are frustrating.

** END IMPORTANT **

 == To Run ==

1. type make
2. look at results.
3. done :)

 == END To Run ==

 ~~ Questions ~~

1. I chose a cryptographic hash function (SHA 256). The output range for SHA 256 is 256. The size of the bloom filter depended on the size of the amount of passwords I was going to store inside of the filter. 
The equation is inside of the code and I linked the website where I got the equation from. Based on the constants (number of bad passwords, number of hashes, and percent error) I was able to know the optimized size of the bit array. It should scale to whatever input you give it as well.

2. The three hash bloom filter took an average time of about .00001s for every password it had to check. The five hash bloom filter took a little longer at an average of .00003s for every password. One performs better than the other because it has to compute two more hashes every single time. 

3. The probability for false positive in my bloom filter was set at ,01 or 1%. You can check the math from the website I linked in the code. I could have gone lower, but then the program would have taken up A LOT more memory. As always for every bloom filter false negatives are not possible.

4. I could reduce the rate of false positives in this instance by increasing the bit size of the array (taking up memory) or increase the number of hashes computer every time to reduce the number of collisions (using up CPU time). I have the false positive rate set as a constant in the code, so it can be changed and the bloom filter will naturally adjust only the size of the bit array to match the rate. To really optimize we would have to mess with number of hashes, size of the bit array, and number of bad passwords given. Since two of those were already given to us we could only manipulate the bit array size (within reason).

 ~~ END Questions ~~
