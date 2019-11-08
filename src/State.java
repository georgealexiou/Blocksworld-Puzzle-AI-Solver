import java.util.ArrayList;

public interface State{

    //returns if the current state is the goal state
    boolean isGoal();

    //returns the children of the current state
    ArrayList<State> genSuccessors();

    //determine cost from initial state to current state
    double determineCost();

    //prints the current state
    void printState();

    //compare states
    boolean isEqual(State s);

}
