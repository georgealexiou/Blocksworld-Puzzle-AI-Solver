package Basic;

import java.io.File;
import java.io.PrintStream;

public class Test {

    public static void main(String[] args){
        try {

            State s1 = new State(new int[]{1,1,1,2,1,3,2,2}, 4);
            System.out.println(s1.toString() + "\n\n");
            State s2 = new State(new int[]{1,1,1,2,1,3,2,1}, 4);
            System.out.println(s1.toString() + "\n\n");
            State s3 = new State(new int[]{1,1,1,2,1,3,2,2}, 4);
            System.out.println(s2.toString() + "\n\n");

            System.out.println("Is s1 = s2: " + s1.equals(s2));
            System.out.println("Is s1 = s2: " + s1.equals(s3));
            System.out.println("Is s2 = s3: " + s1.equals(s3) + "\n");

            System.out.println("Move up");
            s1.makeMove(Move.UP);
            System.out.println(s1.toString() + "\n");

            System.out.println("Move left");
            s1.makeMove(Move.LEFT);
            System.out.println(s1.toString() + "\n");

            System.out.println("Move down");
            s1.makeMove(Move.DOWN);
            System.out.println(s1.toString() + "\n");

            System.out.println("Move down");
            s1.makeMove(Move.DOWN);
            System.out.println(s1.toString() + "\n");

            System.out.println("Move right");
            s1.makeMove(Move.RIGHT);
            System.out.println(s1.toString() + "\n");

            System.out.println("Move right");
            s1.makeMove(Move.RIGHT);
            System.out.println(s1.toString() + "\n\n");

            System.out.println("Move down");
            s1.makeMove(Move.DOWN);
            System.out.println(s1.toString() + "\n");

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
