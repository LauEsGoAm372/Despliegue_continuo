from funcioncitas import  menor_de_arreglo

def test_menor_de_arreglo():
    assert menor_de_arreglo([1,2,4,85,9,0]) == 0
    assert menor_de_arreglo([4,8,6,7,8,31]) == 4