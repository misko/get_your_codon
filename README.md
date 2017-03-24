# get_your_codon
Have you ever needed to encode a secret message into DNA codons? 

Well I did.

Encode the message 'whats shaking'
```
bash-3.2$ python get_your_codon.py 'whats shaking'
Message: whats shaking
Decoded message: 
Encoded message: UGGCACGCUACUUCAUAGUCACACGCUAAGAUUAAUGGC
Encoded/Decoded message WHATS SHAKING
```

Encode/Decode the message 'UGGCACGCUACUUCAUAGUCACACGCUAAGAUUAAUGGC'
```
bash-3.2$ python get_your_codon.py 'UGGCACGCUACUUCAUAGUCACACGCUAAGAUUAAUGGC'
Message: UGGCACGCUACUUCAUAGUCACACGCUAAGAUUAAUGGC
Decoded message: WHATS SHAKING
Encoded message: GUAGGCGGCUGUGCUUGUGGCUGUGUAGCUUGUGUAGUAUGUGCUGUAGCUGGCGUAUGUGCUUGUGCUUGUGGCUGUGUAGCUGCUGGCGCUGUAGUAGCUGCUGUAGGCGGCUGU
Encoded/Decoded message VGGCACGCVACVVCAVAGVCACACGCVAAGAVVAAVGGC
```
