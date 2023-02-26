# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        ans = []
        stc = [root]
        while (len(stc) > 0):
            tstc = []
            for a in stc:
                if (a == None):
                    ans.append("N")
                else:
                    ans.append(str(a.val))
                if (a != None):
                    tstc.append(a.left)
                    tstc.append(a.right)
            stc = tstc
        ans = "x".join(ans)
        return ans

    def deserialize(self, data):
        data = data.split("x")
        if (data[0] == "N"):
            return None
        root = TreeNode(data[0])
        stc = [root]
        i = 1
        while (len(stc) > 0):
            if (data[i] != "N"):
                stc[0].left = TreeNode(int(data[i]))
                i += 1
                stc.append(stc[0].left)
            else:
                stc[0].left = None
                i += 1
            if (data[i] != "N"):
                stc[0].right = TreeNode(int(data[i]))
                i += 1
                stc.append(stc[0].right)
            else:
                stc[0].right = None
                i += 1
            stc.pop(0)
        return root


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(
        3,
        TreeNode(4),
        TreeNode(5),
    ),
)
ans = deser.deserialize(ser.serialize(root))
print(ans)

ser = Codec()
deser = Codec()
root = None
ans = deser.deserialize(ser.serialize(root))
print(ans)