package Basic;

import java.util.Arrays;
import java.util.Objects;

/**
 * The State class represents the state in the Blocksworld Puzzle meaning that it holds the positions of all the blocks a,b,c as well as the agent.
 * The class contains the necessary parameters to represents the puzzle grid as well as methods that allow the agent to move or check whether a mvoe
 * can be performed.
 */
public class State {

    //grid is a 2D array representing the positions of the block and the agent
    private Block[][] grid;
    private int gridSize;
    private int arraySize;

    //Stores information for a, b, c, agent blocks
    private Block a, b, c, agent;

    /*
        @param blockPositions: int[] will be a 1D array where the first two elements will be the
                                     x and y positions of a, then b, then c, then agent
     */

    /**
     * Constructor for Block class that takes the positions of blocks, gridSize and throws an Exception
     *
     * @param blockPositions 1D array where the first two elements will be the x and y positions of a,
     *                       then b, then c, then agent
     * @param gridSize world size of the 2d array (array is going to be of size gridSize * gridSize)
     * @throws Exception exception is thrown when blocks a,b,c,agent overlap (IllegalArgumentException)
     */
    public State(int[] blockPositions, int gridSize) throws Exception{

        this.gridSize = gridSize;
        this.arraySize = gridSize - 1;

        //throw exception if a position is greater than the gridSize
        for (int position: blockPositions){
            if (position > arraySize || position < 0)
                throw new IllegalArgumentException("Error: one or more of the parameters you entered is not within the range 0 and " + arraySize + "." );
        }

        this.a = new Block('A', blockPositions[0], blockPositions[1]);
        this.b = new Block('B', blockPositions[2], blockPositions[3]);
        this.c = new Block('C', blockPositions[4], blockPositions[5]);
        this.agent = new Block('P', blockPositions[6], blockPositions[7]);

        //checks if the blocks are in the same positions
        if(a.equals(b) || a.equals(c) || b.equals(c))
            throw new IllegalArgumentException("Error: Each block should have a different position within the grid.");

        //checks if the blocks are in the same positions as the agent
        else if(agent.equals(a) || agent.equals(b) || agent.equals(c))
            throw new IllegalArgumentException("Error: The blocks and the agent should be at different positions");

        //since everything is correct, we add the blocks to the grid
        else{
            grid = new Block[this.gridSize][this.gridSize];

            //set all positions as empty
            for (int xPos=0; xPos<gridSize; xPos++)
                for (int yPos=0; yPos<gridSize; yPos++)
                    setPosition('x', xPos, yPos);

            //set a,b,c,agent positions
            setPosition(a);
            setPosition(b);
            setPosition(c);
            setPosition(agent);

        }
    }

    /**
     * Method that sets position of a block if it doesn't exist in the grid
     *
     * @param name name of block
     * @param xPos x coordinate of block
     * @param yPos y coordinate of block
     */
    public void setPosition(char name, int xPos, int yPos){
        Block newBlock = new Block (name, xPos, yPos);
        grid[yPos][xPos] = newBlock;

        //if block is a,b,c we update the Blocks a,b,c
        if(name == 'a')
            a = newBlock;

        else if (name == 'b')
            b = newBlock;

        else if(name == 'c')
            c = newBlock;
    }


    /**
     * Method that sets position of a block if it already exists in the grid
     *
     * @param block takes the block coordinates and adds it to the grid
     */
    public void setPosition(Block block){ grid[block.getyPosition()][block.getxPosition()] = block; }

    /**
     * Method that checks if the current state is equal to another state including the agent
     *
     * @param s state that we will compare to
     * @return true if the blocks a,b,c,agent are equal
     *         false if the blocks a,b,c,agent are not equal
     */
    public boolean isEqualFixedAgent(State s){
        return this.a.equals(s.a) && b.equals(s.b) && b.equals(s.b) && c.equals(s.c) && agent.equals(s.agent);
    }

    /**
     * Method that checks if the current state is equal to another state excluding the agent
     *
     * @param s state that we will compare to
     * @return true if the blocks a,b,c are equal
     *         false if the blocks a,b,c are not equal
     */
    public boolean isEqualNoAgent(State s){
        return this.a.equals(s.a) && b.equals(s.b) && b.equals(s.b) && c.equals(s.c);
    }

    /**
     * Method that locates the blocks on the grid given x/y coordinates
     *
     * @param x X coordinate of block
     * @param y Y coordinate of block
     * @return
     */
    public Block locateBlock (int x, int y){
        return grid[y][x];
    }

    /**
     * Method that takes a type of Move and moves the agent depending on the type of move after checking
     * that the agent is not blocked.
     *
     * @param move takes enum Move that shows the type of move we want to perform
     * @return true if the move is made
     *         false if the move is blocked
     */
    public boolean makeMove (Move move){
        Block toReplace = null;

        if(isBlocked(move)){
            System.out.println("move blocked");
            return false;
        }

        else {
            switch (move) {
                case UP:
                    toReplace = locateBlock(agent.getxPosition(), agent.getyPosition() - 1);

                    //placed agent in new position
                    agent.setyPosition(agent.getyPosition() - 1);
                    setPosition(agent);

                    //placed other block in agent's previous position
                    setPosition(toReplace.getName(), toReplace.getxPosition(), toReplace.getyPosition() + 1);


                    break;

                case DOWN:

                    toReplace = locateBlock(agent.getxPosition(), agent.getyPosition() + 1);

                    //placed agent in new position
                    agent.setyPosition(agent.getyPosition() + 1);
                    setPosition(agent);

                    //placed other block in agent's previous position
                    setPosition(toReplace.getName(), toReplace.getxPosition(), toReplace.getyPosition() - 1);

                    break;

                case LEFT:
                    toReplace = locateBlock(agent.getxPosition() - 1, agent.getyPosition());

                    //placed agent in new position
                    agent.setxPosition(agent.getxPosition() - 1);
                    setPosition(agent);

                    //placed other block in agent's previous position
                    setPosition(toReplace.getName(), toReplace.getxPosition() + 1, toReplace.getyPosition());

                    break;

                case RIGHT:
                    toReplace = locateBlock(agent.getxPosition() + 1, agent.getyPosition());

                    //placed agent in new position
                    agent.setxPosition(agent.getxPosition() + 1);
                    setPosition(agent);

                    //placed other block in agent's previous position
                    setPosition(toReplace.getName(), toReplace.getxPosition() - 1, toReplace.getyPosition());

                    break;
            }
        }

        return true;
    }

    /**
     * Checks whether the move is blocked and returns the appropreate boolean
     *
     * @param move Move enum that shows the type of move that the agent wants to perform
     * @return true if the move is blocked
     *         false if the move is not blocked
     */
    public boolean isBlocked(Move move){
        switch(move){
            case UP:
                if(agent.getyPosition() == 0)
                    return true;
                break;

            case DOWN:
                if(agent.getyPosition() == arraySize)
                    return true;
                break;

            case LEFT:
                if(agent.getxPosition() == 0)
                    return true;
                break;

            case RIGHT:
                if(agent.getxPosition() == arraySize)
                    return true;
                break;

            default:
                break;
        }

        return false;
    }

    /**
     * Method that returns a string containing the block positions as well as grid
     *
     * @return string of the grid as well as block positions
     */
    public String toString() {

        String gridString = "";
        for (int i=0; i<gridSize; i++){
            for (int j=0; j<gridSize; j++){
                if (j != arraySize)
                    gridString = gridString + " " + grid[i][j].getName();
                else
                    gridString = gridString + " " + grid[i][j].getName() + "\n";
            }
        }

        String blockPositions = "The positions of each block is shown below: \n" +
                                "    A -> x: " + this.a.getxPosition() + " y: " + this.a.getyPosition() + "\n" +
                                "    B -> x: " + this.b.getxPosition() + " y: " + this.a.getyPosition() + "\n" +
                                "    C -> x: " + this.c.getxPosition() + " y: " + this.a.getyPosition() + "\n" +
                                "    Agent -> x: " + this.agent.getxPosition() + " y: " + this.agent.getyPosition();

        return gridString + "\n\n" + blockPositions;
    }

    //get method for block A
    public Block getA() { return a; }

    //get method for block B
    public Block getB() { return b; }

    //get method for block C
    public Block getC() { return c; }

    //get method for agent block (P)
    public Block getAgent() { return agent; }

    //get method for gridSize
    public int getGridSize() { return gridSize; }

    //get method for arraySize
    public int getArraySize() { return arraySize; }

    //generated automatically using IntelliJ
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        State state = (State) o;
        return gridSize == state.gridSize &&
                arraySize == state.arraySize &&
                Arrays.equals(grid, state.grid) &&
                Objects.equals(a, state.a) &&
                Objects.equals(b, state.b) &&
                Objects.equals(c, state.c) &&
                Objects.equals(agent, state.agent);
    }

    //generated automatically using IntelliJ
    @Override
    public int hashCode() {
        int result = Objects.hash(gridSize, arraySize, a, b, c, agent);
        result = 31 * result + Arrays.hashCode(grid);
        return result;
    }
}
