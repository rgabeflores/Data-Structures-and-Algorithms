
public class BST {

	public static enum TraversalType { PREORDER, INORDER, POSTORDER; }
	
	private Node mRoot;
	
	/**
	 * Constructs a Binary Search Tree
	 */
	public BST()
	{
		mRoot = new Node("");
	}
	
	/**
	 * Adds a key to the tree
	 * @param key the key to add
	 */
	public void insert(String key)
	{
		if(key == null || key.length() < 1) return;
		mRoot.insert(key);
	}
	
	/**
	 * Checks if the specified key is present in the tree
	 * @param key the data to check for
	 * @return whether or not the key is present
	 */
	public boolean isPresent(String key)
	{
		if(key == null) return false;
		return mRoot.found(key);
	}
	
	/**
	 * Traverses through the tree in the specified traversal type
	 * @param type the order to traverse in
	 */
	public void traverse(TraversalType type)
	{
		
		if(type == TraversalType.PREORDER) System.out.print("\nPREORDER tree traversal");
		else if(type == TraversalType.INORDER) System.out.print("\nINORDER tree traversal");
		else if(type == TraversalType.POSTORDER) System.out.print("\nPOSTORDER tree traversal");
		System.out.println();
		mRoot.traverse(type);
		System.out.println();
	}
	
	/**
	 * Gets the number of keys in the tree
	 * @return
	 */
	public int getCount()
	{
		return mRoot.count() - 1;
	}
	
	/**
	 * Removes the specified key from the tree
	 * @param key the key to be removed
	 */
	public void remove(String key)
	{
		if(key == null || key.length() < 1) return;
		mRoot.find(key).remove();
	}
	
	// Node Class
	private class Node
	{	
		private String mData;
		private Node mLeft;
		private Node mRight;
		private Node mParent;
		
		public Node(String data)
		{
			mData = data;
			mLeft = mRight = mParent = null;
		}
		
		public void insert(String key)
		{
			if(key.compareTo(mData) < 0)
			{
				if(mLeft == null)
				{
					mLeft = new Node(key);
					mLeft.mParent = this;
				}
				else 
				{
					mLeft.insert(key);
				}
			}
			else
			{
				if(mRight == null)
				{
					mRight = new Node(key);
					mRight.mParent = this;
				}
				else
				{
					mRight.insert(key);
				}
			}
		}
		
		public void remove()
		{
			if(mLeft == null && mRight == null) //CASE 1: Node is a leaf
			{
				if(mData.compareTo(mParent.mData) > 0) // Compares to parent to see if it is left or right of parent
				{
					mParent.mRight = null;
				}
				else
				{
					mParent.mLeft = null;
				}
			}
			else if(mLeft == null && !(mRight == null)) //CASE 2: Node does not have mLeft but does have mRight
			{
				if(mData.compareTo(mParent.mData) > 0) // Compares to parent to see if it is left or right of parent
				{
					mRight.mParent = mParent; 
					mParent.mRight = mRight; 
				}
				else
				{
					mRight.mParent = mParent;  
					mParent.mLeft = mRight; 
				}
			}
			else if(!(mLeft == null) && mRight == null) //CASE 3: Node does not have mRight but does have mLeft
			{
				if(mData.compareTo(mParent.mData) > 0) // Compares to parent to see if it is left or right of parent
				{
					mLeft.mParent = mParent; 
					mParent.mRight = mRight; 
				}
				else
				{
					mLeft.mParent = mParent;  
					mParent.mLeft = mLeft; 
				}
			}
			else //CASE 4: Node has both mRight and mLeft
			{
				Node replacement = mLeft.findRightMost(); // Gets the right most node of the left sub tree
				if(mData.compareTo(mParent.mData) > 0) // Compares to parent to see if it is left or right of parent
				{
					mData = replacement.mData; // Note: only mData is touched Make new node? Completely switch node?
				}
				else
				{
					mData = replacement.mData;
				}
				replacement.remove();
			}
		}
		
		public void traverse(TraversalType type)
		{
			if(type == TraversalType.PREORDER) visit(this);
			if(mLeft != null)
			{
				mLeft.traverse(type);
			}
			
			if(type == TraversalType.INORDER) visit(this);
			if(mRight != null)
			{
				mRight.traverse(type);
			}
			
			if(type == TraversalType.POSTORDER) visit(this);
		}
		
		public int count()
		{
			if(mLeft == null && mRight == null) return 1;
			else if(mLeft != null)
			{
				if(mRight != null)	return 1 + mLeft.count() + mRight.count();				
				else	return 1 + mLeft.count();
			}
			return 1 + mRight.count();
		}
		
		public boolean found(String key)
		{
			if(key.equals(""))	return true;
			else if(mLeft == null && mRight == null)	return false;
			else if(key.compareTo(mData) == 0)	return true;
			else if(key.compareTo(mData) < 0)
			{
				if(mLeft == null)	return false;
				return mLeft.found(key);
			}
			else
			{
				if(mRight == null)	return false;
				return mRight.found(key);
			}
			
		}
		
		private Node find(String key)
		{
			if(key.compareTo(mData) == 0)	return this;
			else if (key.compareTo(mData) < 0)	return mLeft.find(key);
			return mRight.find(key);
		}
		
		private Node findRightMost()
		{
			if(mRight == null)	return this;
			return mRight.findRightMost();
		}
		
		private void visit(Node node)
		{
			if(node.mData == null || node.mData.length() < 1) return;
			System.out.print(node.mData + " ");
		}
	}
}
