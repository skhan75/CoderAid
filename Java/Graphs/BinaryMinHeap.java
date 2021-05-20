/**
 *
 * Data structure to support following operations
 * extracMin - O(logn)
 * addToHeap - O(logn)
 * containsKey - O(1)
 * decreaseKey - O(logn)
 * getKeyWeight - O(1)
 *
 * It is a combination of binary heap and hash map
 */
import java.util.*;

public class BinaryMinHeap<T> {
	private List<Node> allNodes = new ArrayList<>();
	private Map<T,Integer> nodePosition = new HashMap<>();
	int size;

	BinaryMinHeap() {
		this.size = 0;
	}

	public class Node {
		int weight;
		T key;

		Node(int weight, T key) {
			this.weight = weight;
			this.key = key;
		}
	}

	public boolean isLeaf(int pos) {
        if (pos >= (size / 2) && pos <= size) {
            return true;
        }
        return false;
    }

	void add(int weight, T key) {
		Node node = new Node(weight, key);
		allNodes.add(node);
		size = allNodes.size();
		int current = size - 1;
		int parentIndex = (current-1) / 2;
		nodePosition.put(node.key, current);

		while(parentIndex>=0) {
			Node parentNode = allNodes.get(parentIndex);
			Node currentNode = allNodes.get(current);

			if(parentNode.weight > currentNode.weight) {
				swap(parentNode, currentNode);
				updatePositionMap(parentNode.key, currentNode.key, parentIndex, current);
				current = parentIndex;
				parentIndex = (parentIndex-1)/2;
			} else {
				break;
			}
		}
	}

	private Node extractMin() {
		int size = allNodes.size() -1;
        Node minNode = new Node(allNodes.get(0).weight, allNodes.get(0).key);

        int lastNodeWeight = allNodes.get(size).weight;
        allNodes.get(0).weight = lastNodeWeight;
        allNodes.get(0).key = allNodes.get(size).key;
        nodePosition.remove(minNode.key);
        nodePosition.remove(allNodes.get(0));
        nodePosition.put(allNodes.get(0).key, 0);
        allNodes.remove(size);

		int currentIndex = 0;
		size--;

		while(true){
            int left = 2*currentIndex + 1;
            int right = 2*currentIndex + 2;
            if(left > size){
                break;
            }
            if(right > size){
                right = left;
            }
            int smallerIndex = allNodes.get(left).weight <= allNodes.get(right).weight ? left : right;
            if(allNodes.get(currentIndex).weight > allNodes.get(smallerIndex).weight){
                swap(allNodes.get(currentIndex), allNodes.get(smallerIndex));
                updatePositionMap(allNodes.get(currentIndex).key,allNodes.get(smallerIndex).key,currentIndex,smallerIndex);
                currentIndex = smallerIndex;
            }else{
                break;
            }
        }

		// minHeapify(currentIndex);

		return minNode;
	}

	private void minHeapify(int pos) {
		if(!isLeaf(pos)) {
			int leftChildIndex = (2*pos)+1;
			int rightChildIndex = (2*pos)+2;

			int smallerWeightNodeIndex = allNodes.get(leftChildIndex).weight < allNodes.get(rightChildIndex).weight ? leftChildIndex : rightChildIndex;
			if(allNodes.get(pos).weight > allNodes.get(smallerWeightNodeIndex).weight) {
				swap(allNodes.get(pos), allNodes.get(smallerWeightNodeIndex));
				updatePositionMap(allNodes.get(pos).key,allNodes.get(smallerWeightNodeIndex).key,pos,smallerWeightNodeIndex);
				minHeapify(smallerWeightNodeIndex);
			}
		}
	}

	private void swap(Node node1,Node node2){
        int weight = node1.weight;
        T data = node1.key;
        
        node1.key = node2.key;
        node1.weight = node2.weight;
        
        node2.key = data;
        node2.weight = weight;
    }

    private void updatePositionMap(T key1, T key2, int val1, int val2){
        nodePosition.remove(key1);
        nodePosition.remove(key2);
        nodePosition.put(key1, val1);
        nodePosition.put(key2, val2);
    }

    public void printHeap(){
        for(Node n : allNodes){
            System.out.println(n.weight + " " + n.key);
        }
    }

    private void printPositionMap(){
        System.out.println(nodePosition);
    }


	public static void main(String[] args) {
		BinaryMinHeap<String> heap = new BinaryMinHeap<String>();
        heap.add(3, "Tushar");
        heap.add(4, "Ani");
        heap.add(8, "Vijay");
        heap.add(10, "Pramila");
        heap.add(5, "Roy");
        heap.add(6, "NTF");
        heap.add(2,"AFR");
        heap.printHeap();
        heap.printPositionMap();

        System.out.println("Extracted Min --> "+heap.extractMin().key);
        heap.decrease("Pramila", 1);
        System.out.println("Extracted Min --> "+heap.extractMin().key);
	}
}