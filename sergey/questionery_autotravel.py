#1. Описание бизнеса

graf = {}
graf[childrens] = ['0+'=1 cat, '6+'=2 cat, '9+'=3 cat]
graf[teenagers] = ['12+'=4 cat, '15+'=5 cat]
graf[students] = ['18+'=6 cat]
graf[grownups] = ['25+'=7 cat,'36+'=8 cat, '46+'=9 cat,'56+'=10 cat, '66+'=7 cat]

node = find_lowest_node(costs)#найти узел с наименьшей стоимостью среди необработанных
while node is not None:#если обработаны все узлы цикл while завершен
    cost = costs[node]
    neighbors = graf[node]
    for n in neighbors.keys():#перебрать всех соседей текущего узла
        new_cost = cost + neyghbors[n]#если к соседу можно быстрее добраться через текущий узел...
        if cost[n] > new_cost:
        cost[n] = new_cost#...обновить стоимость для этого узла
        parents[n] = node#этот узел становится новым родителем для соседа
processed.append(node)#узел помечается как обработанный
node = find_lowest_cost_node(costs)#найти следующий узел для обработки и повторить цикл