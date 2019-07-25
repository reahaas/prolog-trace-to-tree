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


# Text to image
The next problem is how to present the huge text tree in one screen, in a zoomable image, that will allow us to zoom out to see the full tree structure, and to zoom in to see the actual function calls.
After some searches I found this link, that create an image from the text:
https://onlinetexttools.com/convert-text-to-image

# The final results are:
Look how beautifull is end's up:

![q2_trace_there_is_way](https://user-images.githubusercontent.com/35425887/61906076-35a96e80-af33-11e9-84f8-2a1a323669ac.png)

![q3_trace_monkey](https://user-images.githubusercontent.com/35425887/61906086-3c37e600-af33-11e9-9239-4f5e091acef3.png)
