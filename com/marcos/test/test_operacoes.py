def funcao(var):
	return var + 5

def test1_positivo():
	assert func(10) == 15

def test_negativo():
	assert func(-10) == -5

def test_zero():
	assert func(0) == 5