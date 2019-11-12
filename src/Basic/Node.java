package Basic;

import java.util.ArrayList;
import java.util.Objects;

/**
 * The Node Class is used to represent nodes in a search tree when running the different algorithms.
 * The class contains a state, meaning the state of the puzzle, a parent meaning the previous node,
 * the path cost to this node, the depth of the node in the search tree, the previous move taken and
 * the heuristic cost to the end node.
 */
public class Node implements Comparable{

    //characteristics of a Node
    private State state;
    private Node parent;
    private int pathCost;
    private int depth;

    private Move previousMove; //move taken from parent Node to current Node
    private int heuristic; //heuristic cost to final node


    /**
     * Constructor for class Node that is the root of the search tree
     *
     * @param state the current state of the puzzle
     */
    public Node(State state) {
        this.state = state;
        this.depth = 0;
        this.pathCost = 0;
    }

    /**
     * Constructor for the class Node that isn't the root of the tree (has parent node)
     *
     * @param state the current state of the puzzle
     * @param previousMove the move made from the parent Node to current Node
     * @param parent the parent node of the current node
     */
    public Node(State state, Move previousMove, Node parent) {
        this.state = state;
        this.parent = parent;
        this.previousMove = previousMove;

        if(parent != null) {
            this.pathCost = parent.pathCost + 2;
            this.depth = parent.depth + 1;
        }
    }

    //method that returns whether the Node is the root of the search tree
    private boolean isRoot(){ return this.parent == null; }

    //get method that returns the state
    public State getState() { return state; }

    //get method that returns parent Node
    public Node getParent() { return parent; }

    //get method that returns the pathCost
    public int getPathCost() { return pathCost; }

    //get method that returns the depth of the node
    public int getDepth() { return depth; }

    //get method that returns the previous move made from parent to current Node
    public Move getPreviousMove() { return previousMove; }

    /**
     * Method that calculates the heuristic cost from the current Node (this) to a target node.
     * The heuristic cost is calculated by adding the distances from each block of this Node to the target Node.
     * We also add the depth of the current Node.
     *
     * @param node target node to calculate heuristic to
     */
    public void calculateHeuristicEstimate(Node node) {

        int heuristic = 0;

        //adding the distances for blocks of this Node to target Node
        heuristic += node.getState().getA().getxPosition() - getState().getA().getxPosition();
        heuristic += node.getState().getA().getyPosition() - getState().getA().getyPosition();
        heuristic += node.getState().getB().getxPosition() - getState().getB().getxPosition();
        heuristic += node.getState().getB().getyPosition() - getState().getB().getyPosition();
        heuristic += node.getState().getC().getxPosition() - getState().getC().getxPosition();
        heuristic += node.getState().getC().getyPosition() - getState().getC().getyPosition();

        //adding current node depth to heuristic
        heuristic += getDepth();

        this.heuristic = heuristic;
    }

    /**
     * Method that returns an ArrayList of characters representing the moves made from the root to the current Node.
     *
     * @return ArrayList<Character> of all moves made to reach solutions
     */
    public ArrayList<Character> displayPathTaken(){

        ArrayList<Character> path = new ArrayList<Character>();
        Node current = this;
        path.add(convertMoveToChar(current.getPreviousMove()));

        while (current.getParent() != null){
            this.depth = parent.getDepth() + 1;
            path.add(convertMoveToChar(current.getPreviousMove()));
        }

        return path;
    }

    /**
     * Method that converts a move enum to a character for use in the displayPathTaken() method.
     * The conversions are as follows:
     *     Move.UP = 'U'
     *     Move.DOWN = 'D'
     *     Move.LEFT = 'L'
     *     Move.RIGHT = 'R'
     *
     * @param move Move enum used to understand what to return
     * @return character representing the move input to the method
     *
     */
    public char convertMoveToChar(Move move){
        switch(move){
            case UP:
                return 'U';

            case DOWN:
                return 'D';

            case LEFT:
                return 'L';

            case RIGHT:
                return 'R';
        }

        return 'x';
    }

    /**
     * Method that generates and ArrayList that contains the possible moves that can be made from the current Node
     * If the move is possible (using isBlocked from the State class), then a node is generated and added to the ArrayList.
     *
     * @return ArrayList<Node> that represents the moves that can be made from the current Node
     */
    public ArrayList<Node> getPossibleMoves(){

        ArrayList<Node> possibleMoves = new ArrayList<>();

        try {

            if (!state.isBlocked(Move.UP)) {
                Node upNode = new Node(state, Move.UP, this);
                upNode.state.makeMove(Move.UP);
                possibleMoves.add(upNode);
            }

            if (!state.isBlocked(Move.DOWN)) {
                Node downNode = new Node(state, Move.DOWN, this);
                downNode.state.makeMove(Move.UP);
                possibleMoves.add(downNode);
            }

            if (!state.isBlocked(Move.LEFT)) {
                Node leftNode = new Node(state, Move.LEFT, this);
                leftNode.state.makeMove((Move.LEFT));
                possibleMoves.add(leftNode);
            }

            if (!state.isBlocked((Move.RIGHT))) {
                Node rightNode = new Node(state, Move.RIGHT, this);
                rightNode.state.makeMove((Move.RIGHT));
                possibleMoves.add(rightNode);
            }

        }catch(Exception e){
            System.out.println(e.getMessage());
        }

        return possibleMoves;
    }


    /**
     * We use the compareTo method from the Comparable interface implemented in the beggining of the class. This is done
     * to help us compare the current Node with a different Node. We compare the nodes in terms of their heuristic cost.
     *
     * @param o we compare our current node to this node (we convert it from Object to Node)
     * @return -1 if the current node has a smaller heuristic cost
     *         0 if the current node has the same heuristic cost
     *         1 if the current node has a greater heuristic cost
     */
    @Override
    public int compareTo(Object o){
        Node node = (Node) o;

        if (heuristic == node.heuristic) return 0;
        else if (heuristic > node.heuristic) return 1;
        else return -1;
    }

    //generated automatically using IntelliJ
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Node node = (Node) o;
        return Objects.equals(state, node.state);
    }

    //generated automatically using IntelliJ
    @Override
    public int hashCode() {
        return Objects.hash(state);
    }
}
