import sys
from tabulate import tabulate

sys.path.append('../../BCC__BCC36B__P[2]__HenriqueMarcuzzo_2046334/impl/')

import tppSintatic
import SimbolTable

# GLOBAL
variable_table_list = list()
funcion_table_list = list()
escope = 'global'


# OLD

def find_node(node, label):
    exist = False

    if node is None:
        return exist, None

    for sun in node.children:
        exist, return_node = find_node(sun, label)

        if sun.label == label:
            exist = True
            return_node = sun

        if exist:
            return exist, return_node

    return exist, None


def find_all_nodes(root, label, list_node):
    for node in root.children:
        list_node = find_all_nodes(node, label, list_node)
        if node.label == label:
            list_node.append(node)

    return list_node


def find_all_filter_nodes(root, label, father_label, list_node):
    all_nodes = find_all_nodes(root, label, list_node)

    i = 0
    len_list = len(all_nodes)

    while i < len_list:
        if all_nodes[i].ancestors[-1].label != father_label:
            all_nodes.pop(i)

            len_list -= 1
            i -= 1

        i += 1

    return all_nodes


def find_father(sun, label_father):
    if sun is None:
        return None

    for node in sun.ancestors:
        if node.label == label_father:
            return node
        father_node = find_father(node, label_father)

        if father_node is not None and father_node.label == label_father:
            return father_node

    return None


def get_func_type(node):
    type_func = node.children[0].children[0].children[0]

    if type_func.label != 'inteiro' and type_func.label != 'inteiro':
        type_func.label = 'vazio'

    return type_func


def find_func(root, name_func):
    all_nodes = find_all_nodes(root, 'declaracao_funcao', list())
    list_func_with_same_name = list()
    for node in all_nodes:
        exist, return_node = find_node(node, name_func)

        if exist:
            list_func_with_same_name.append(node)

    return list_func_with_same_name


def has_principal(root):
    principal_nodes = find_func(root, 'principal')

    if len(principal_nodes) < 1:
        message = ('ERROR', 'Erro: Função principal não declarada.')
        message_list.append(message)
    elif len(principal_nodes) == 1:
        type_func = get_func_type(principal_nodes[0]).label
        all_retorna_nodes = find_all_filter_nodes(principal_nodes[0], 'retorna', 'acao', list())

        if len(all_retorna_nodes) < 1:
            message = ('ERROR', f'Erro: Função principal deveria retornar {type_func}, mas retorna vazio.')
            message_list.append(message)
        else:
            for node in all_retorna_nodes:
                if type_func == 'inteiro':
                    all_wrong_type = find_all_nodes(node, 'NUM_PONTO_FLUTUANTE', list())
                else:
                    all_wrong_type = find_all_nodes(node, 'NUM_INTEIRO', list())

                if len(all_wrong_type) > 0:
                    message = (
                    'ERROR', f'Erro: Função principal deveria retornar apenas {type_func}, mas retorna outro tipo.')
                    message_list.append(message)
                    return

            return principal_nodes[0]


def identifie_all_functions(root):
    for node in root.children:
        identifie_all_functions(node)

        if node.label == 'declaracao_funcao':
            name_func = find_node(node, 'ID')[-1].children[0].label
            type_func = get_func_type(node).label
            # parameter_func =
            print(type_func)


## NEW

def clean_tuple(lst):
    return [t for t in (set(tuple(i) for i in lst))]


def get_var_in_scope(element, escopo='global'):
    for var in var_list[element]:
        if var[4] == escopo:
            return var


def generate_table_func(list, header, list_index):
    table = [header]

    for element in list:
        for func in list[element]:
            aux_array = []
            for index in list_index:
                aux_array.append(func[index])
            table.append(aux_array)

    return table


def generate_table_var(list, header, list_index):
    table = [header]

    for element in list:
        for func in list[element]:
            aux_array = []
            for index in list_index:
                if index == 3:
                    dim_tam = []
                    for j in range(len(func[index])):
                        if func[index][j][1] == 'NUM_PONTO_FLUTUANTE':
                            value = float(func[index][j][0])
                        else:
                            value = int(func[index][j][0])
                        dim_tam.append(value)
                    aux_array.append(dim_tam)
                else:
                    aux_array.append(func[index])
            table.append(aux_array)

    return table


def main():
    global func_list, var_list, message_list

    root, func_list, var_list, message_list = tppSintatic.main()

    # Checar se as chamadas estão no escopo correto caso contrario trocar os escopos
    for element in var_list:
        for index_var in range(len(var_list[element])):
            escopo_atual = var_list[element][index_var][4]
            if escopo_atual != 'global':
                len_call_list = len(var_list[element][index_var][-1])
                tuple_call_index = 0

                while tuple_call_index < len_call_list:
                    tuple_call = var_list[element][index_var][-1][tuple_call_index]
                    if func_list[escopo_atual][0][5] <= tuple_call[0] < func_list[escopo_atual][0][6]:
                        pass
                    else:
                        new_var_escopo = get_var_in_scope(element, 'global')
                        new_var_escopo[-1].append(tuple_call)
                        var_list[element][index_var][-1].pop(tuple_call_index)
                        len_call_list -= 1
                        tuple_call_index -= 1

                    tuple_call_index += 1

    # # Remover tuplas iguais das chamadas de variaveis
    # for element in var_list:
    #     for index_var in range(len(var_list[element])):
    #         var_list[element][index_var][-1] = clean_tuple(var_list[element][index_var][-1])

    func_table = generate_table_func(func_list, ['Nome', 'Tipo', 'Num. Parâmetros', 'Parâmetros', 'Init',
                                                 'Linha Inicial', 'Linha Final'], [0, 1, 2, 3, 7, 5, 6])

    var_list = generate_table_var(var_list, ['Nome', 'Tipo', 'Dimensões', 'Tamanho Dimensões', 'Escopo', 'Linha'],
                                   [0, 1, 2, 3, 4, 5])

    print(f'TABELA DE FUNÇÕES:\n{tabulate(func_table, headers="firstrow", tablefmt="fancy_grid")}')
    print('\n\n')
    print(f'TABELA DE VARIÁVEIS:\n{tabulate(var_list, headers="firstrow", tablefmt="fancy_grid")}')
    print('\n\n')

    message_list = clean_tuple(message_list)
    for message in message_list:
        print(message[-1])


if __name__ == '__main__':
    main()
