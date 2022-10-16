def f(a:list,b:list):
    sum=a+b
    remove_doubles=[[] if sum[id] in sum[0:id] else [sum[id]] for id in range(len(sum))]
    return [x**3 for week_element in remove_doubles for x in week_element]

print (f([1,2],[4,1,3]))
