from pprint import pprint


def determine(data, deter):

    min_v = float('inf')
    min_i = 'chave'
    for k, v in data.items():
        if v['deter'] or v['valor'] == 0 or v['nome'] in deter:
            v['deter'] = False
            continue

        if v['valor'] < min_v:
            min_v = v['valor']
            min_i = k

    if min_v == float('inf'):
        return data
    data[min_i]['deter'] = True
    return data


def shortest_way(matriz, data):

    deter = set()
    while True:
        if not set([i['nome'] for i in data.values()]).difference(deter):
            break

        deter_session = [i for i in data.values() if i['deter'] is True][0]
        deter.add(deter_session['nome'])

        for i, v in enumerate(matriz[int(deter_session['index'])]):
            i = str(i)
            if v == 0 or data[str(i)]['nome'] == deter_session['vem']:
                continue

            if data[i]['vem'] != data[deter_session['index']]['nome']:
                valor = v + data[deter_session['index']]['valor']
                if data[i]['valor'] > valor:
                    data[i]['valor'] = valor
                    data[i]['vem'] = data[deter_session['index']]['nome']

        data = determine(data, deter)

    return data


if __name__ == '__main__':
    matriz = [
        [0, 1, 2, 0],
        [1, 0, 0, 4],
        [2, 0, 0, 1],
        [0, 4, 1, 0]
    ]

    data = {
        '0': {'deter': True, 'nome': 'A', 'vem': 'A', 'valor': 0, 'index': '0'},
        '1': {'deter': False, 'nome': 'B', 'vem': None, 'valor': float('inf'), 'index': '1'},
        '2': {'deter': False, 'nome': 'C', 'vem': None, 'valor': float('inf'), 'index': '2'},
        '3': {'deter': False, 'nome': 'D', 'vem': None, 'valor': float('inf'), 'index': '3'}
    }
    matriz = [
        [0, 5, 6, 10, 0, 0, 0],
        [5, 0,  0, 0, 13, 0, 0],
        [6, 0, 0, 3, 11, 6, 0],
        [10, 0, 3, 0, 6, 4, 0],
        [0, 13, 11, 6, 0, 0, 3],
        [0, 0, 6, 4, 0, 0, 8],
        [0, 0, 0, 0, 3, 8, 0]
    ]

    data = {
        '0': {
            'deter': True, 'nome': 'J', 'vem': 'J',
            'valor': 0, 'index': '0'
        },
        '1': {
            'deter': False, 'nome': 'A', 'vem': None,
            'valor': float('inf'), 'index': '1'
        },
        '2': {
            'deter': False, 'nome': 'P', 'vem': None,
            'valor': float('inf'), 'index': '2'
        },
        '3': {
            'deter': False, 'nome': 'Q', 'vem': None,
            'valor': float('inf'), 'index': '3'
        },
        '4': {
            'deter': False, 'nome': 'B', 'vem': None,
            'valor': float('inf'), 'index': '4'
        },
        '5': {
            'deter': False, 'nome': 'C', 'vem': None,
            'valor': float('inf'), 'index': '5'
        },
        '6': {
            'deter': False, 'nome': 'E', 'vem': None,
            'valor': float('inf'), 'index': '6'
        }
    }

    shortest_way(matriz, data)
    pprint(data)
