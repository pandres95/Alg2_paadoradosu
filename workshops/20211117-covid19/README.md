# Taller Grupal 1: Covid-19

```python
def find (target, sequence):
    for i in range(len(sequence)):
        counter = 0
        
        for j in range(i, min(i + len(target), len(sequence))):
            if target[j - i] == sequence[j]:                        # O(1)
                counter += 1                                        # O(1)
        
            if counter == len(target):                              # O(1)
                return (i, i + len(target) - 1)                     # O(1)
    
    return (-1, -1)
```

```python
def find (target, sequence):
    for i in range(len(sequence)):
        counter = 0
        
        for j in range(i, min(i + len(target), len(sequence))):     # h(n) = O(min{i + len(target); len(sequence)}) * O(4) = O(min{i + len(target); len(sequence)})
            if target[j - i] == sequence[j]:                        # O(1)
                counter += 1                                        # O(1)
        
            if counter == len(target):                              # O(1)
                return (i, i + len(target) - 1)                     # O(1)
    
    return (-1, -1)
```

```python
def find (target, sequence):
    for i in range(len(sequence)):                                  # g(n) = O(len(sequence)) * (O(1) + h(n)) = O(n²)
        counter = 0                                                 # O(1)
        
        for j in range(i, min(i + len(target), len(sequence))):     # h(n) = O(min{i + len(target); len(sequence)}) * O(4) = O(min{i + len(target); len(sequence)})
            if target[j - i] == sequence[j]:                        # O(1)
                counter += 1                                        # O(1)
        
            if counter == len(target):                              # O(1)
                return (i, i + len(target) - 1)                     # O(1)
    
    return (-1, -1)
```

Para calcular $f(n)$, tenemos que:

1. $O(len(sequence)) * (1 + O(min{i + len(target); len(sequence)})) = O(len(sequence)) * 1 + O(len(sequence)) * O(min{i + len(target); len(sequence)})$
2. $O(len(sequence)) * 1 = O(len(sequence))$
3. $O(min{i + len(target); len(sequence)}) = O(k)$, donde $k = min{i + len(target); len(sequence)}$
4. $O(len(sequence)) * O(k) = O(len(sequence))$
5. $g(n) = O(len(sequence)) * O(len(sequence))$, entendido como $(4) * (2)$

Ahora, se puede entender a `len(sequence)` como `n`, por lo que:

6. `g(n) = O(n) * O(n) = O(n * n) = O(n²)`


```python
def find (target, sequence):                                        # f(n) = O(n²) + O(1) = max{O(n²), O(1)} = O(n²)
    for i in range(len(sequence)):                                  # g(n) = O(len(sequence)) * (O(1) + h(n)) = O(n²)
        counter = 0                                                 # O(1)
        
        for j in range(i, min(i + len(target), len(sequence))):     # h(n) = O(min{i + len(target); len(sequence)}) * O(4) = O(min{i + len(target); len(sequence)})
            if target[j - i] == sequence[j]:                        # O(1)
                counter += 1                                        # O(1)
        
            if counter == len(target):                              # O(1)
                return (i, i + len(target) - 1)                     # O(1)
    
    return (-1, -1)                                                 # O(1)
```

Finalmente, concluímos que la complejidad de `find` es de $O(n²)$.