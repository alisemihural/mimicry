# Mimicry

**Proposed method on How to score Mimicry:**

1. Moves (out of 100): Each move is graded separately irrespective of the order they are executed. (for 5 total moves in the original pattern (movement sequence), each move (action) is considered to be 20 points; for 3 moves total in the original pattern, every move is 33.3 points, etc.)
   1. If the action (unit movement) is correct but made on the wrong side, get half points. 
   1. If the action is done half of the entire unit movement (not done entirely), gets half points as well.
   1. If a move is missing or wrong completely, no points.
1. Order of the moves (out of 100): Are the moves (actions) in the intended (original sequence) order? Each move is graded separately with the same distribution as above.
1. Extra move penalty: Penalize the score per each extra unnecessary action (movement), with the same amount of weight of valid action (for 5 movements, every action it is -20 points, for 3 actions every extra action is -33.3 points, etc.)

**Total Score: Moves + Order + Extra (maximum is 200 points)**

**Examples: Intended pattern is 1 2 3 4 5**

1. Participant does 1 2 3 4 5, all the sides are correct

Moves: 100 points (5/5 moves are made)

Order: 100 points

Extra : 0 points (no penalty)

**Total: 200/200 points**

1. Participant does 1 2 3 5, all the sides are correct

Moves: 80 points (4/5 moves are made)

Order: 100 points

Extra : 0 points (no penalty)

**Total: 180/200 points**

1. Participant does 1 2 3 6 4 5, all the sides are correct

Moves: 100 points  (5/5 moves are made)

Order: 100 points

Extra : -20 points (one extra move)

**Total: 180/200 points**

1. Participant does 1 2 6 4 5, all the sides are correct

Moves: 80 points  (4/5 moves are made)

Order: 100 points

Extra: -20 points (one extra move)

**Total: 160/200 points**

1. Participant does 1 2 4 3 5, all the sides are correct

Moves: 100 points (5/5 moves are made)

Order: 60 points

Extra: 0 points (no penalty)

**Total: 160/200 points**

1. Participant does 1 2 4 3 4 5, all the sides are correct

Moves: 100 points (5/5 moves are made)

Order: 100 points

Extra: -20 points (no penalty)

**Total: 180/200 points**

1. Participant does 1 2 6 5 4 3, all the sides are correct

Moves: 100 points (5/5 moves are made)

Order: 40 points

Extra : -20 points (one extra move)

**Total: 120/200 points**

1. Participant does 2 3 4 6 5, all the sides are correct

Moves: 80 points (4/5 moves are made)

Order: 100 points (Only 1 is not there)

Extra : -20 points (one extra move)

**Total: 160/200 points**

1. Participant does 2 3 4 6 5, only the side for move 3 is incorrect

Moves: 70 points (3/5 moves are made, action #3 gets half points) ( 20\*3 + 20/2 \* 1 = 70)

Order: 100 points (Only 1 is not there)

Extra: -20 points (one extra move)

**Total: 150/200 points**
