package Basic;

import java.util.Arrays;
import java.util.Objects;

public class State {

    //grid and blocks
    private Block[][] grid;
    private int gridSize;
    private int arraySize;
    private Block a, b, c, agent;

    /*
        @param blockPositions: int[] will be a 1D array where the first two elements will be the
                                     x and y positions of a, then b, then c, then agent
     */
    public State(int[] blockPositions, int gridSize) throws Exception{

        this.gridSize = gridSize;
        this.arraySize = gridSize-1;

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
            for (int xPos=0; xPos<arraySize; xPos++)
                for (int yPos=0; yPos<arraySize; yPos++)
                    setPosition('x', xPos, yPos);

            //set a,b,c,agent positions
            setPosition(a);
            setPosition(b);
            setPosition(c);
            setPosition(agent);

        }
    }

    //setPosition method if Block doesn't exist
    public void setPosition(char name, int xPos, int yPos){
        Block newBlock = new Block (name, xPos, yPos);
        grid[xPos][yPos] = newBlock;

        if(name == 'a')
            a = newBlock;

        else if (name == 'b')
            b = newBlock;

        else if(name == 'c')
            c = newBlock;
    }

    //setPosition method if Block already exists
    public void setPosition(Block block){
        grid[block.getxPos()][block.getyPos()] = block;
    }

    public boolean isEqualFixedAgent(State s){
        return this.a.equals(s.a) && b.equals(s.b) && b.equals(s.b) && c.equals(s.c) && agent.equals(s.agent);
    }

    public boolean isEqualNoAgent(State s){
        return this.a.equals(s.a) && b.equals(s.b) && b.equals(s.b) && c.equals(s.c);
    }

    public Block locateBlock (int xPos, int yPos){
        return grid[xPos][yPos];
    }

    public boolean makeMove (Move move) throws Exception{
        Block toReplace = null;

        if(isBlocked(move))
            return false;

        else {
            switch (move) {
                case UP:
                    toReplace = locateBlock(agent.getxPos(), agent.getyPos() + 1);

                    //placed agent in new position
                    agent.setyPos(agent.getyPos() + 1);
                    setPosition(agent);

                    //placed other block in agent's previous position
                    setPosition(toReplace.getName(), toReplace.getxPos(), toReplace.getyPos() - 1);
                    break;

                case DOWN:
                    toReplace = locateBlock(agent.getxPos(), agent.getyPos() - 1);

                    //placed agent in new position
                    agent.setyPos(agent.getyPos() - 1);
                    setPosition(agent);

                    //placed other block in agent's previous position
                    setPosition(toReplace.getName(), toReplace.getxPos(), toReplace.getyPos() + 1);
                    break;

                case LEFT:
                    toReplace = locateBlock(agent.getxPos() - 1, agent.getyPos());

                    //placed agent in new position
                    agent.setxPos(agent.getxPos() - 1);
                    setPosition(agent);

                    //placed other block in agent's previous position
                    setPosition(toReplace.getName(), toReplace.getxPos() + 1, toReplace.getyPos());
                    break;

                case RIGHT:
                    toReplace = locateBlock(agent.getxPos() + 1, agent.getyPos());

                    //placed agent in new position
                    agent.setxPos(agent.getxPos() + 1);
                    setPosition(agent);

                    //placed other block in agent's previous position
                    setPosition(toReplace.getName(), toReplace.getxPos() - 1, toReplace.getyPos());
                    break;
            }
        }

        return true;
    }

    public boolean isBlocked(Move move){
        switch(move){
            case UP:
                if(agent.getyPos() == 0)
                    return true;
                break;

            case DOWN:
                if(agent.getyPos() == arraySize)
                    return true;
                break;

            case LEFT:
                if(agent.getxPos() == 0)
                    return true;
                break;

            case RIGHT:
                if(agent.getxPos() == arraySize)
                    return true;
                break;

            default:
                break;
        }

        return false;
    }

    public String toString() {
        String gridString = this.grid[0][0] + " " + this.grid[0][1] + " " + this.grid[0][2] + " " + this.grid[0][3] + "\n" +
                            this.grid[1][0] + " " + this.grid[1][1] + " " + this.grid[1][2] + " " + this.grid[1][3] + "\n" +
                            this.grid[2][0] + " " + this.grid[2][1] + " " + this.grid[2][2] + " " + this.grid[2][3] + "\n" +
                            this.grid[3][0] + " " + this.grid[3][1] + " " + this.grid[3][2] + " " + this.grid[3][3];

        String blockPositions = "The positions of each block is shown below: \n" +
                                "    A -> x: " + this.a.getxPos() + " y: " + this.a.getyPos() + "\n" +
                                "    B -> x: " + this.b.getxPos() + " y: " + this.a.getyPos() + "\n" +
                                "    C -> x: " + this.c.getxPos() + " y: " + this.a.getyPos() + "\n" +
                                "    Agent -> x: " + this.agent.getxPos() + " y: " + this.agent.getyPos();

        return gridString + "\n\n" + blockPositions;
    }

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
