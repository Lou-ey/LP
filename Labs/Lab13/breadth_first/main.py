from tree import TreeNode
from bfs import bfs

sample_root_node = TreeNode("Home")
docs = TreeNode("Documents")
photos = TreeNode("Photos")
sample_root_node.children = [docs, photos]
my_wish = TreeNode("WishList.txt")
my_todo = TreeNode("TodoList.txt")
my_cat = TreeNode("Fluffy.jpg")
my_dog = TreeNode("Spot.jpg")
docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]

# Write your code below.
print(sample_root_node)
# goal_path = bfs(sample_root_node, 'Z') (ALteracao do parametro "goal_value" para "Home")
# goal_path = bfs(sample_root_node, 'Home') (ALteracao do parametro "goal_value" para "Fluffy.jpg")
goal_path = bfs(sample_root_node, 'Fluffy.jpg')

if not goal_path:
    print('No path found')
else:
    print('Path found')
    for node in goal_path:
        print(node.value)