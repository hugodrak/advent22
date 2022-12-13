"""
{'name': 'test',
 'type': 'folder',
 'content': [{'name': 'subfolder_1',
   'type': 'folder',
   'content': [{'name': 'test_file_1.txt', 'type': 'file'},
    {'name': 'test_file_2.txt', 'type': 'file'}]},
  {'name': 'subfolder_2',
   'type': 'folder',
   'content': [{'name': 'test_file_3.txt', 'type': 'file'}]}]}
   """
global total
total = 0
def find_index(cont, name):
    i = 0
    for d in cont:
        if d['name'] == name:
            return i
        i += 1

def update_tree(cwd, tree):
    if len(cwd) == 0:
        return
    current = cwd[-1]
    content_keys = []
    if current == tree['name']:
        return update_tree(cwd[:-1], tree)

    for c in tree['content']:
        content_keys.append(c['name'])
    if current not in content_keys:
        tree['content'].append({"name":current, "type": "dir", "size": 0, "content": []})
    else:
        i = find_index(tree['content'], current)
        return update_tree(cwd[:-1], tree['content'][i])

    #"name":"/", "type": "dir", "__size__": 0, "content": []
    
    
def add_files_to_tree(cwd, tree, values):
    global total
    if len(cwd) == 0:
        return
    elif len(cwd) == 1:
        tot_size = 0
        for val in values:
            tot_size += val['size']
            tree['content'].append(val)
        tree['size'] += tot_size
        return 
    else:
        i = find_index(tree['content'], cwd[-2])
        add_files_to_tree(cwd[:-1], tree['content'][i], values)
        tree['size'] += tree['content'][i]['size']
        return 

def find_sizes(tree):
    global total
    contents = tree['content']
    for c in contents:
        if c['type'] == "dir":
            find_sizes(c)
    if tree['size'] <= 100000:
        total += tree['size']
        print(tree['name'], tree['size'])



if __name__ == "__main__":
    small = open("small", "r").read().split("$")
    lines = open("input", "r").read().split("$")
    tree = {"name":"/", "type": "dir", "size": 0, "content": []}
    cwd = []
    # ' ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n'
    for cmd in lines:
        if len(cmd) < 3:
            continue
        rows = cmd.split("\n")
        match cmd[1:3]:
            case "cd":
                path = rows[0].split(" ")[2]
                if path == "..":
                    _ = cwd.pop()
                else:
                    cwd.append(path)
                    update_tree(cwd[::-1], tree)

            case "ls":
                values = []
                for row in rows[1:-1]:
                    if len(row) >= 4:
                        if row[:3] == "dir":
                            path = row.split(' ')[1]
                            cwd.append(path)
                            update_tree(cwd[::-1], tree)
                            _ = cwd.pop()
                        else:
                            sp = row.split(" ")
                            values.append({"name": sp[1], "type": "file", "size": int(sp[0])})
                add_files_to_tree(cwd[::-1], tree, values)
    h=0
    find_sizes(tree)
    print(total)


