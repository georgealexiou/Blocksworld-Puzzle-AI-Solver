package Basic;

import java.io.File;
import java.io.PrintStream;
import java.util.ArrayList;

import SearchAlgorithms.AStarSearch;
import SearchAlgorithms.BFSearch;

public class Test {

    public static void main(String[] args){
        try {

            State s1 = new State(new int[]{1,1,1,2,1,3,2,2}, 4);

            System.out.println(s1.toString() + "\n\n");
            /*State s2 = new State(new int[]{0,3,1,3,2,3,3,3}, 4);
            System.out.println(s1.toString() + "\n\n");
            State s3 = new State(new int[]{1,1,1,2,1,3,2,2}, 4);
            System.out.println(s2.toString() + "\n\n");

            System.out.println("Is s1 = s2: " + s1.equals(s2));
            System.out.println("Is s1 = s2: " + s1.equals(s3));
            System.out.println("Is s2 = s3: " + s1.equals(s3) + "\n");
            */

            Node n1 = new Node(s1);
            ArrayList<Node> moves = n1.getPossibleMoves();

            for (Node move: moves){
                System.out.println(move.toString());
            }

            /*
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
            */

            State start = new State(new int[]{0,3,1,3,2,3,3,3}, 4);
            State finish = new State(new int[]{1,1,1,2,1,3,3,3}, 4);

            Node start1 = new Node (start);
            Node finish1 = new Node (finish);

            
            //BFSearch bfs = new BFSearch(start1, finish1);
            //System.out.println(bfs.isFound());
            //BFSearch bfs = new BFSearch();
            AStarSearch aStar = new AStarSearch();




        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
