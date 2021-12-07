# Taller Grupal 2: Búsqueda en Arbol Binario

## Cálculo

```py
class Node:
    def __init__(self, data):
        self._data = data                              #----------- O(1)
        self.left = None                               #----------- O(1)
        self.right = None                              #----------- O(1)

    @property
    def data(self):
        return self._data                              #----------- O(1)

    def find(root, key):
        path = []                                      #----------- O(1)
        while root != None:                            #----------- O(n)
            if key > root.data:                        #----------- O(1)
                path.append('Derecha')                 #----------- O(1)
                root = root.right                      #----------- O(1)
            elif key < root.data:                      #----------- O(1)
                path.append('Izquierda')               #----------- O(1)
                root = root.left                       #----------- O(1)
            else: return (True, path)                  #----------- O(1)
        return (False, path)                           #----------- O(1)

    def insert(node, data):
        if node == None:                               #----------- O(1)
            return Node(data)                          #----------- O(1)
        
        if data < node.data:                           #----------- O(1)
            node.left = Node.insert(node.left, data)   #----------- O(1)
        elif data > node.data:                         #----------- O(1)
            node.right = Node.insert(node.right, data) #----------- O(1)
        
        return node                                    #----------- O(1)
        

def main():
    root_data = int(input('Ingrese el valor raiz para la generacion del arbol binario: '))   #---------- O(1)
    
    root = Node(root_data)                                                                   #---------- O(1)

    for i in range(int(input('Cantidad nodos para la generación del arbol binario: '))):     #---------- O(n)
        root.insert(int(input('Ingrese el valor ({}): '.format(i + 1))))                     #---------- O(1)

    search_key = int(input('Diga cuál valor desea buscar en el arbol: '))                    #---------- O(1)

    (found, path) = Node.find(root, search_key)                                              #---------- O(n)

    if found:
        print('La ruta del valor buscado desde el origen es:')                               #---------- O(1)
    else:
        print('No se ha encontrado el valor buscado. La ruta explorada desde el origen es:') #---------- O(1)
    print(' '.join(path))                                                                    #---------- O(1)

main()
```

Así es como `f(n)`, definido como `main` es **O(n)**, como se describe en el cálculo dado a continuación:

```
f(n) = O(1) + O(1) + O(n) + O(1) + O(1) + O(n) + O(1) + O(1) + O(1)
f(n) = O(7) + 2 * O(n)
f(n) = 2 * O(n)
f(n) = O(n)
```

## Explicación 
La complejidad de `find` es **O(n)**. Esto se debe a que, si bien, normalmente la búsqueda en un árbol binario sería **O(log(n))**, esto es cierto para los casos de un árbol binario de búsqueda (es decir, un árbol binario, que es a la vez ordenado y balanceado). En este caso, el peor escenario ocurre cuando todos los nodos que se insertaron debajo de la raíz son menores, o mayores, y se trata de buscar el nodo con el dato más pequeño o grande del arbol, o un dato que no existe en el árbol, dando así con un recorrido sobre todos los nodos antes de encontrarlo o no encontrarlo.

