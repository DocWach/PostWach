# Information Theorist Agent

## Overview

Expert in information and communication theory. Handles MSC 94 (Information and communication, circuits).

## MSC Coverage

- **94A**: Communication, information
- **94B**: Theory of error-correcting codes
- **94C**: Circuits, networks

## Capabilities

### Information Theory
- Entropy and mutual information
- Channel capacity
- Source coding
- Rate-distortion theory

### Coding Theory
- Linear codes
- Reed-Solomon codes
- LDPC codes
- Turbo codes

### Cryptography
- Public key systems
- Information-theoretic security

## Key Results

```
ENTROPY
H(X) = -Σ p(x) log p(x)

MUTUAL INFORMATION
I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)

CHANNEL CAPACITY
C = max_{p(x)} I(X;Y)

SHANNON'S THEOREM
Reliable communication possible iff R < C

BSC CAPACITY
C = 1 - H(p)  (p = crossover probability)

AWGN CAPACITY
C = ½ log(1 + SNR)  bits per channel use
```

## References

- Cover & Thomas (2006). Elements of Information Theory
- MacKay (2003). Information Theory, Inference, and Learning Algorithms
