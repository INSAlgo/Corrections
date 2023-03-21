""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root, left = -1, right=10**4+1):
    if root is None:    # Si une feuille de l'arbre
        return True
    if root.data<=left or root.data>=right:     # Si pas dans l'intervalle
        return False
    # Sinon, on vérifie les enfants
    return check_binary_search_tree_(root.left, left, root.data) \
        and check_binary_search_tree_(root.right, root.data, right)

