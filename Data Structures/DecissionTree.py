# el decission tree teoricamente es un BST?
# intentar implementar

#* Arbol de Decisión Simple
# Determinar día de la semana.
class DecissionNode:
    def __init__(self, condition=None, condition_text = "", result=None):
        self.condition = condition
        self.condition_text = condition_text
        self.result = result
        self.left = None
        self.right = None

def eval_decission_tree(node: DecissionNode, value):
    # Si no hay condición, es una hoja: devolvemos el resultado.
    if node.condition is None:
        return node.result
    # Si la condición se cumple, seguimos por la rama izquierda; si no, por la derecha.
    if node.condition(value):
        return eval_decission_tree(node.left, value)
    else:
        return eval_decission_tree(node.right, value)
    
def print_decission_tree(node: DecissionNode, prefix: str = "", isLeft: bool = True, value = None):
    # Paramos la recursión si no hay un nodo.
    if node is None:
        return
    branch = "└── " if not isLeft else "├── "
    if node.condition:
        print(prefix + branch + node.condition_text)
    else:
        if node.result.lower() == value.lower():
            print(prefix + branch + node.result + " ✅")
        else:
            print(prefix + branch + node.result)
    
    if node.left or node.right:
        separator = "    " if not isLeft else "|   "
        new_prefix = prefix + separator
        if node.left:
            print_decission_tree(node.left, new_prefix, True, value=value)
        if node.right:
            print_decission_tree(node.right, new_prefix, False, value=value)

#* Construcción del DecissionTree
# Nodo Raíz que segmenta los días en 1-4 y 5-7
root = DecissionNode(lambda day: day <= 4, "day <= 4")

#* Ramas para días 1 a 4:
# Determinamos si el día está en el segmento 1-2 o 3-4.
decision_left = DecissionNode(lambda day: day <= 2, "day <= 2")

#* Días 1 y 2.
# Ditsinguimos entre Lunes y Martes
node_1_2 = DecissionNode(lambda day: day == 1, "day == 1")
node_1_2.left = DecissionNode(result="Lunes") # Si day == 1 es True; por ende day = Lunes
node_1_2.right = DecissionNode(result="Martes") # Si day == 1 es False; por ende day = Martes

#* Días 3 y 4
# Distinguimos entre Miércoles y Jueves
node_3_4 = DecissionNode(lambda day: day == 3, "day == 3")
node_3_4.left = DecissionNode(result="Miércoles") # Si day == 3 es True; por ende day = Miércoles
node_3_4.right = DecissionNode(result="Jueves") # Si day == 3 es False; por ende day = Jueves

# Conectamos las ramas para el grupo 1-4
decision_left.left = node_1_2   # Si day <= 2 es True, evaluamos días 1 o 2
decision_left.right = node_3_4  # Si day <= 2 es False, evaluamos días 3 o 4

#* Ramas para días 5 a 7:
# Distinguimos si el día es 5 o no
decision_right = DecissionNode(lambda day: day == 5, "day == 5")
decision_right.left = DecissionNode(result="Viernes") # Si day == 5 es True; por ende es Viernes

#* Días 6 y 7
# Distinguimos entre 6 y 7.
node_6_7 = DecissionNode(lambda day: day == 6, "day == 6")
node_6_7.left = DecissionNode(result="Sábado") # Si day == 6 es True; por ende es Sábado
node_6_7.right = DecissionNode(result="Domingo") # Si day == 6 es False; por ende es Domingo

# Asignamos la rama derecha:
decision_right.right = node_6_7  # Si day == 5 es False, evaluamos días 6 o 7

#? Conectamos las ramas al nodo raíz:
root.left = decision_left
root.right = decision_right

result = eval_decission_tree(root, 1)

print_decission_tree(root, value=result)