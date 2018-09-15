# Algorithms and their common Applications / Use Cases:

We have read and used various different algorithms and dynamic programming problems via school, college and interview preps. And the sample use case asked in the problem is too brief and naive to understand the actual real world use case. <br/>
<br/>Lets take a simple example. We all have used "auto spell check", either on our phones or computers. Its a perfect instance of the "Minimum Edit Distance" problem using "Levenshtein Distance" . You get corrections for mis-spelled words from a dictionary that have low distance to word in question.

Below are the few commonly used algorithms from our day to day life:


## Minimum Edit Distance
* It is a way of quantifying how dissimilar two strings are to one another.

* It works on <b>Levenshtein Distance</b> algorithm, which basically gives you the difference (edit distance) between two strings i.e. how many minimum INSERT, DELETE and SUBSTITUTE operations are required to turn one string into another.<br/>
For example, The Levenshtein distance between <i>kitten</i> and <i>sitting</i> is 3. In Levenshtein's original definition each of these operations are unit cost, which means: <br/>
  * SUBSTITUTE 'k' for 's' --> +1 operation
  * SUBSTITUTE 'e' for 'i' --> +1 operation
  * INSERT 'g' --> +1 operation

  #### Applications
  * In natural language processing, where automatic spelling correction can determine candidate corrections for a misspelled word by selecting words from a dictionary that have a low distance to the word in question.
  * In bioinformatics, it can be used to quantify the similarity of DNA sequences, which can be viewed as strings of the letters A, C, G and T.
  * Evaluating Machine Translation and Speech Recognition.

  #### Example
  Lets say we have two strings `abcdef` and `azced` as <b>s1</b> and <b>s2</b>, represented in a 2D matrix <b>T</b>.

  |   |   | a | b | c | d | e | f |
  |---|---|---|---|---|---|---|---|
  |   | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
  | a | 1 | 0 | 1 | 2 | 3 | 4 | 5 |
  | z | 2 | 1 | 1 | 2 | 3 | 4 | 5 |
  | c | 3 | 2 | 2 | 1 | 2 | 3 | 4 |
  | e | 4 | 3 | 3 | 2 | 2 | 2 | 3 |
  | d | 5 | 4 | 4 | 3 | 2 | 3 | <b>3<b> |


  We then compute the INSERT, DELETE and SUBSTITUTE operations.
  * If s1[ i ] == s2[ j ], we copy the operation # at T[ i-1 ] [ j-1 ]
  * Else, we take the value of
    ```python
    1 + min (
      T[ i-1 ] [ j-1 ], T[ i ] [ j-1 ], T [ i-1 ] [ j-1 ]
    )
    ```
  In above example, the answer is 3.


## Longest Common Subsequence
* Finding the longest subsequence common to all sequences in a set of sequences (often just two sequences).

  #### Applications
  * The longest common subsequence problem is a classic computer science problem, the basis of data comparison programs such as the `diff utility`.
  * It is also widely used by revision control systems such as <b>Git</b> for reconciling multiple changes made to a revision-controlled collection of files.
  * In Molecular biology, DNA sequences (genes) can be represented as sequences of four letters ACGT, corresponding to the four submolecules forming DNA. When biologists find a new sequences, they typically want to know what other sequences it is most similar to. One way of computing how similar two sequences are is to find the length of their longest common subsequence.
    * S1 = AAACCGTGAGTTATTCGTTCTAGAA

      S2 = CACCCCTAAGGTACCTTTGGTTC

      LCS is ACCTAGTACTTTG
