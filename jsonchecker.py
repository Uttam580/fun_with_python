import json , os , sys

if len(sys.argv)>1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], 'r')
        json.load(file)
        file.close()
        print('validate json')
    else:
        print(sys.argv[1]+'not found')
else:
    print('Usages : checkjson.py')