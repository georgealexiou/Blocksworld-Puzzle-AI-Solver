import java.util.ArrayList;

public class PuzzleState implements State {
    @Override
    public boolean isGoal() {
        return false;
    }

    @Override
    public ArrayList<State> genSuccessors() {
        return null;
    }

    @Override
    public double determineCost() {
        return 0;
    }

    @Override
    public void printState() {

    }

    @Override
    public boolean isEqual(State s) {
        return false;
    }
}
