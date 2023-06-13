import json
import os



path = os.listdir('input')
path = sorted(path)


for file in path:

    # load input file
    f = open(f'input/{file}')
    data = json.load(f)


    # create file for output
    newF = open(f'output/{file}-output.txt', 'w')
    des = data['description']
    newF.write(f'{des}:\n\n')


    # write action of problem
    newF.write(f'Actions:\n')
    action = data['actions']
    
    for item in action:
        newF.write(f'"{item}" is an action.\n')
    newF.write('\n')


    # write mechanisms of problem
    newF.write(f'Mechanisms:\n')
    mechanism = dict(data['mechanisms'])
    
    for k,v in mechanism.items():
        if type(v) == str:
            newF.write(f'"{k}" if "{v}"\n')
        
        elif type(v) == list:
            newF.write(f'"{k}" if ')
            for item in v[0:len(v) - 1:]:
                newF.write(f'"{item}" or ')
            lastItem = v[len(v) - 1]
            newF.write(f'"{lastItem}"\n')
    newF.write('\n')


    # write Utilities of problem
    newF.write(f'Utilities:\n')
    utility = dict(data['utilities'])
    
    # utils = list(utility)[::-1]
    
    # while len(utils) > 0:
    #     a = utils.pop()
    #     b = utils.pop()
    #     if utility[a] > utility[b]:
    #         newF.write(f'"{a}" is good\n')
    #         newF.write(f'"{b}" is bad\n')
    #     else:
    #         newF.write(f'"{a}" is bad\n')
    #         newF.write(f'"{b}" is good\n')

    maximum = float('-inf')
    key = None

    for k, v in utility.items():
        if v > maximum:
            maximum = v
            key = k
    
    newF.write(f'"{key}" is good\n')
    for k, v in utility.items():
        if v != maximum:
            newF.write(f'"{k}" is bad\n')
    newF.write('\n')



    # write best choise of problem
    
    # maximum = float('-inf')
    # key = None
    
    # for k,v in utility.items():
    #     if v > maximum:
    #         maximum = v
    #         key = k

    newF.write(f'The best choise is "{key}" with {maximum} score.\n\n')


    # write intention of problem
    intentionConseq = []
    
    for k,v in mechanism.items():
        if type(v) == str:
            if v == key:
                intentionConseq.append(k)
        elif type(v) == list:
            if key in v:
                intentionConseq.append(k)
    for k,v in mechanism.items():
        if type(v) == str:
            if v in intentionConseq and not k in intentionConseq:
                intentionConseq.append(k)
        elif type(v) == list:
            for item in v:
                if v in intentionConseq and not k in intentionConseq:
                    intentionConseq.append(k)
    newF.write(f'The intention of this problem for action "{key}", consequences: ')
    for item in intentionConseq[0:len(intentionConseq) - 1:]:
        newF.write(f'"{item}" --> ')
    newF.write(f'"{intentionConseq[len(intentionConseq) - 1]}".\n')



print('Outputs save successfully in output directory...')
