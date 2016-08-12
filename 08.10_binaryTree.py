//求二叉树结点个数
def nodeNum(self,root):
	if root is None:
		return 0
	return self.nodeNum(root.left)+self.nodeNum(root.right)+1
//求二叉树深度
def depth(self,root):
	if root is None:
		return 0
	left = self.depth(root.left)
	right = self.depth(root.right)
	if left>right:
		return left+1
	if right>=left:
		return right+1
//求二叉树宽度		
def width(self,root):
	cur = 1
	max = 0
	q = queue.Queue()
	q.put(root)
	while not q.empty():
		n = cur //这里重新赋值，保证n不再变化
		for i in range(n):
			tmp = q.get()
			cur-=1
			if tmp.left:
				q.put(tmp.left)
				cur+=1
			if tmp.right:
				q.put(tmp.right)
				cur+=1
		if cur > max:
			max = cur
	return max
