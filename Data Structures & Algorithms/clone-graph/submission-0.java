/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/
/**
Given a node in a connected undirected graph, return a deep copy of the graph

Deep copy: completely new nodes of the whole graph
    All nodes and edges must be re-created
    Structure must match exactly with the original graph

so each node has an adjaency list i.e. a mapping to its neighbors

*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        HashMap<Node, Node> map = new HashMap<>();
        return dfs(node, map);
        //maps the orignal node to the cloned node
    }
    private Node dfs(Node node, Map<Node, Node> map){
        //If we have already cloned this node, we can just return it
        if(map.containsKey(node)){
            return map.get(node);

        } 
        //Create a mew node with the same value
        Node clone = new Node(node.val);
        map.put(node, clone);

        //next clone all the neighbors
        for(Node nei : node.neighbors){
            clone.neighbors.add(dfs(nei, map));
        }

        return clone;

        


    }
}