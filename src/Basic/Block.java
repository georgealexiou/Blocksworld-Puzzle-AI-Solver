package Basic;

import java.util.Objects;

/**
 * A class representing a Block in a Blocksworld grid. it has the necessary parameters to represent the positions
 * of Blocks in the grid as well as the name of the block.
 */
public class Block {
    //characteristics of block name and coordinates
    private char name;
    private int y;
    private int x;

    /**
     * Constructor of the Block class that takes the name as well as coordinates of a block
     *
     * @param name character representing the name of the class
     * @param x horizontal (x) coordinate of block
     * @param y vertical (y) coordinate of block
     */
    public Block(char name, int x, int y) {
        this.name = name;
        this.y = y;
        this.x = x;
    }

    public char getName() {
        return name;
    }

    //set method for the name of the block
    public void setName(char name) { this.name = name; }

    //get method for the y coordinate of the block
    public int getyPosition() { return y; }

    //set method of the y coordinate of the block
    public void setyPosition(int yPos) { this.y = yPos; }

    //get method for the x coordinate of the block
    public int getxPosition() { return x; }

    //set method for the x coordinate of the block
    public void setxPosition(int xPos) { this.x = xPos; }

    //returns the position of the block
    public String getPosition(){ return getxPosition() + " " + getyPosition(); }

    //generated automatically using IntelliJ
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Block block = (Block) o;
        return y == block.y &&
                x == block.x;
    }

    //generated automatically using IntelliJ
    @Override
    public int hashCode() {
        return Objects.hash(name, y, x);
    }
}
