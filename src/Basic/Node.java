package Basic;

public class Node implements Comparable{

    //charachteristics of a node
    private State state;
    private Node parent;
    private int pathCost;
    private int depth;

    private int heuristic; //heuristic cost of node


    //constructor for root node (does not have parent nodes)
    public Node(State state) {
        this.state = state;
        this.depth = 0;
        this.pathCost = 0;
    }

    //constructor for Node that isn't the root (has parent nodes)
    public Node(State state, Node parent, int pathCost, int depth, int heuristic) {
        this.state = state;
        this.parent = parent;

        if(parent != null) {
            this.pathCost = parent.pathCost + 2;
            this.depth = parent.depth + 1;
        }
    }



    public State getState() {
        return state;
    }

    public Node getParent() {
        return parent;
    }

    public int getPathCost() {
        return pathCost;
    }

    public int getDepth() {
        return depth;
    }

    //I NEED TO CHANGE THIS IT DOESNT WORK
    public int compareTo(Object node){
        if(heuristic < ((Node) node).heuristic) return -1;
        else if(heuristic == ((Node) node).heuristic) return 0;
        else return 1;
    }
}

}
