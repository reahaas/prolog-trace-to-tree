# prolog-trace-to-tree
print the trace from prolog as a tree of calls



I solved it in a different way... I run the program in prolog with trace, that give me an output of the trace as text. Each step in a different line. Save this trace output to a file. it should look like this:

?- trace,there_is_way(telaviv,heifa).
Call: (9) there_is_way(telaviv, heifa) ? creep
Call: (10) there_is_way(telaviv, heifa, nil) ? creep
Call: (11) road_from(telaviv, heifa) ? creep
Call: (12) road(telaviv, heifa) ? creep
Fail: (12) road(telaviv, heifa) ? creep
Fail: (11) road_from(telaviv, heifa) ? creep
Redo: (10) there_is_way(telaviv, heifa, nil) ? creep
Call: (11) road_from(telaviv, _4236) ? creep
Call: (12) road(telaviv, _4236) ? creep


Then use this python code to print the calls trace tree: Its build the tree relying on the first word of the trace: {Call, Fail, Exit, Redo}.

notice: change the file path/name in the code (with open(...)).