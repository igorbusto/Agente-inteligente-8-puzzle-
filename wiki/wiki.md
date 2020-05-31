- # Puzzle 8

    - ## Objetivo:
        - O objetivo do jogo é mover as peças a partir de um estado inicial até encontrar seu estado final, quando o Puzzle está ordenado de forma crescente como na figura abaixo.

<div style="text-align:center;margin:2%;"><img src="images\puzzle8-objetivo.png"/></div>

- # Agentes

    - ## Agente humano:
         Nessa categoria não a interferência da maquina. Apenas as jogadas inseridas pelo jogador são consideradas, W (Cima), A (Esquerda), S (Baixo) D (Direita). Após a sequencia numérica estar completa e correta é exibida a mensagem de vitória ao usuário.

    - ## Agente guloso:
        Trata-se um algoritmo que tenta resolver o problema fazendo a escolha localmente ótima em cada fase com a esperança de encontrar um ótimo global.

        - C é o conjunto de candidatos;
        - S contém conjunto solução, inicialmente vazio;
        - ∃ candidatos e não achou uma solução?;
        - Seleciona o próximo candidato;
        - Remove esse candidato do conjunto C;
        - A solução é viável;
        - Sim, incorpora o candidato à solução;
        - Obteve uma solução?;
        - Sim, retorna a solução;
        - Não, para a execução;

    - ## Agente A* (A estrela):
        Trata-se um algoritmo para busca de caminhos. Ele busca o caminho em um grafo de um vértice inicial até um vértice final. Ele é a combinação de duas aproximações heurísticas, o algoritmo Breadth First Search (Busca em Largura) e da formalidade do Algoritmo de Dijkstra.

        - Inicialize Q com o nó de busca (S) como única entrada;
        - Se Q está vazio, interrompa. Se não, escolha o melhor elemento de Q;
        - Se o estado (n) é um objetivo, retorne n;
        - (De outro modo) Remova n de Q;
        - Encontre os descendentes do estado (n) que não estão em visitados e crie todas as extensões de n para descendente;
        - Adicione os caminhos estendidos a Q e vá ao passo 2;

    - ## Agente BFS:
        Trata-se um algoritmo que garante que nenhum vértice ou aresta seja visitado mais de uma vez e, para isso, utiliza uma estrutura de dados fila para garantir a ordem de chegada dos vértices. 

    - ## Agente DFS:
        Trata-se um algoritmo de busca em profundidade realiza uma busca não-informada que progride através da expansão do primeiro nó filho da árvore de busca, e se aprofunda cada vez mais, até que o alvo da busca seja encontrado ou até que ele se depare com um nó que não possui filhos (nó folha). Então a busca retrocede (backtrack) e começa no próximo nó. Numa implementação não-recursiva, todos os nós expandidos recentemente são adicionados a uma pilha, para realizar a exploração.

    - ## Agente DFS limitado:
        Trata-se de uma estratégia de busca na qual uma versão limitada em profundidade da pesquisa em profundidade é executada repetidamente com o aumento da profundidade limites até que a meta seja encontrada.

    - ## Agente DFS limitado iterativo:
        Trata-se de uma estratégia de busca em que uma versão limitada profundidade de busca em profundidade é executado repetidamente com crescentes limites de profundidade até a objetivo é encontrado.
