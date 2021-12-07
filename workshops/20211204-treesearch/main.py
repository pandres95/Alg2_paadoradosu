class Node:
    def __init__(self, data):
        self._data = data
        self.left = None
        self.right = None

    @property
    def data(self):
        return self._data

    def find(root, key):
        path = []
        while root != None:
            if key > root.data:
                path.append('Derecha')
                root = root.right
            elif key < root.data:
                path.append('Izquierda')
                root = root.left
            else: return (True, path)
        return (False, path)

    def insert(node, data):
        if node == None:
            return Node(data)
        
        if data < node.data:
            node.left = Node.insert(node.left, data)
        elif data > node.data:
            node.right = Node.insert(node.right, data)
        
        return node
        

def main():
    root_data = int(input('Ingrese el valor raiz para la generacion del arbol binario: '))
    
    root = Node(root_data)

    for i in range(int(input('Cantidad nodos para la generación del arbol binario: '))):
        root.insert(int(input('Ingrese el valor ({}): '.format(i + 1))))

    search_key = int(input('Diga cuál valor desea buscar en el arbol: '))

    (found, path) = Node.find(root, search_key)

    if found:
        print('La ruta del valor buscado desde el origen es:')
    else:
        print('No se ha encontrado el valor buscado. La ruta explorada desde el origen es:')
    print(' '.join(path))

main()