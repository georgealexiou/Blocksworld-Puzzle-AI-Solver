package Basic;

import java.util.Objects;

public class Block {
    private char name;
    private int yPos;
    private int xPos;

    public Block(char name, int yPos, int xPos) {
        this.name = name;
        this.yPos = yPos;
        this.xPos = xPos;
    }

    public char getName() {
        return name;
    }

    public void setName(char name) {
        this.name = name;
    }

    public int getyPos() {
        return yPos;
    }

    public void setyPos(int yPos) {
        this.yPos = yPos;
    }

    public int getxPos() {
        return xPos;
    }

    public void setxPos(int xPos) {
        this.xPos = xPos;
    }

    public String getPosition(){
        return getxPos() + " " + getyPos();
    }

    //generated automatically using IntelliJ
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Block block = (Block) o;
        return yPos == block.yPos &&
                xPos == block.xPos;
    }

    //generated automatically using IntelliJ
    @Override
    public int hashCode() {
        return Objects.hash(name, yPos, xPos);
    }
}
