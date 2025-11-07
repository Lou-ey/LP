from TreeNode import TreeNode, sample_root_node, print_path, print_tree

print_tree(sample_root_node)

def dfs(root, target, path=()):
    path = path + (root,)
    if root.value == target:
        return path
    for child in root.children:
        node_found = dfs(child, target, path)
        if node_found:
            return node_found
    return None

goal_path = dfs(sample_root_node, "F")
# goal_path = dfs(sample_root_node, "Z") (Retorna o path como None quando o target nao existe na tree)
print(goal_path)