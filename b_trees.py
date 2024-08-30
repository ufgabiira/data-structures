""" Árvores B

* Uma árvore B é caracterizada por nós que possuem várias chaves.
* Exceto para as folhas, cada nó com k filhos terá k-1 elementos.
* Para os nós internos,
	° a quantidade de filhos estará será k = [M/2, M], logo a quantidade de
    elementos será k-1 = [(M/2)-1, M-1]; e
	° dois nós com o mínimo de elementos podem ser unificados, assim como um 
    nó com o máximo de elementos pode ser separado em dois.
* Para o nó raíz,
	° a quantidade máxima de elementos será a mesma dos nós internos mas não
    existirá um valor mínimo;
	° quando a contagem de elementos for menor que (M/2)-1, para a árvore,
    então ela possuirá apenas o nó raíz.
* Para os nós folha,
	° a profundidade será sempre a mesma, logo cada folha terá a mesma
    quantidade de antecessores.
* O crescimento da árvore B será sempre de baixo para cima. Cada novo nó será
criado como nó pai e não como filho.

Iteração
---------------------
Considere a árvore B na figura.   

    D   H   L
  /   |   |   \
ABC  EFG IJK  MNO

Cada elemento do nó atual em que estamos buscando será comparado com uma chave
de busca.
* Se o elemento comparado for igual a chave, teremos 3 opções: retornar o
elemento ou remover o elemento.
* Se o primeiro elemento for maior que a chave, então iremos para o nó filho no
canto extremo esquerdo;
* se for maior que o primeiro elemento e menor que o segundo, iremos para o
segundo nó da esquerda para a direita;
* se estiver entre o segundo e o terceiro elemento, iremos para o penúltimo nó
filho da esquerda para a direita;
* por último, se a chave for maior que o terceiro elemento, iremos para o nó
filho do canto extremo direito.

Inserção
--------
Começaremos inserindo o novo elemento nos nós folha.
* Se após adicionar o novo elemento, o nó ficar com uma quantidade igual de
filhos e elementos, ele deve ser separado em dois nós e o elemento do meio será
elevado para inserção no nó pai;
	° caso a mesma situação ocorra ao inserir o elemento no nó pai, o passo
    anterior deve ser repertido.
* se não houver um nó pai, significa que inserimos o elemento na raíz, portanto
será preciso criar  um novo nó raíz, que receberá o elemento elevado.

Remoção
-------
* Todo
"""