class MimicryScoreCalculator:
    """
    Calculate:
    - Move Completion
    - Move Side
    - Order
    - Extra Moves
    """

    def __init__(self):
        # We'll store which moves are actually completed 
        # so we can know what's missing
        self.completedSet = set()

    def extraMoveCalculation(self, sequence, length):
        """
        Calculate deductions for extra moves in the sequence.
        Extra moves include repeated or unnecessary moves 
        not in the ideal set of {1..length}.
        """
        idealSet = set(range(1, length + 1))  
        seen = set()   # Track valid moves that are part of the ideal set
        extra_moves = []
        filtered_sequence = []

        # Filter out extra moves + duplicates
        for num in sequence:
            if abs(num) in idealSet and abs(num) not in seen:
                seen.add(abs(num))
                filtered_sequence.append(num)
            else:
                extra_moves.append(num)

        # Deduction is based on the number of extra moves
        deduction = len(extra_moves) * (100 / length)

        print("\n Extra Moves:", extra_moves)
        print("Updated Sequence After Removing Extra Moves:", filtered_sequence)
        return deduction, filtered_sequence

    def moveCalculation(self, sequence, length):
        """
        Calculate move correctness and completion points.
        If the sequence contains negative numbers, 
        deduct half points for those moves.
        """
        idealSet = set(range(1, length + 1))
        completedSet = set()
        points = 0
        move_points = 100 / length

        for num in sequence:
            if abs(num) in idealSet:
                if num > 0:
                    completedSet.add(num)
                    points += move_points
                else:
                    # negative => half points
                    completedSet.add(abs(num))
                    points += move_points / 2

            # Once all moves are done, stop early
            if len(completedSet) == len(idealSet):
                break

        # Keep track of which moves got done (any sign)
        self.completedSet = {abs(x) for x in completedSet}

        print("Completed Set:", self.completedSet)
        print("Sequence Array:", sequence)
        print("Move Points:", points)
        return points

    def completeMissingMoves(self, sequence, length):
        """
        Build a final sequence of exactly 'length' moves for order checking.
        Inserts missing moves in their correct positions based on the ideal order.
        
        Example:
        User types [2, 3, 4, 5] for length=5 -> Result: [1, 2, 3, 4, 5]
        User types [2, 3, 5] for length=5 -> Result: [1, 2, 3, 4, 5]
        """
        ideal_sequence = list(range(1, length + 1))
        user_sequence_set = set(abs(num) for num in sequence)

        # Create the final sequence
        final_sequence = []

        if len(sequence) < length:
            for i in ideal_sequence:
                if i in user_sequence_set:
                    # Keep the user's version (positive or negative)
                    for num in sequence:
                        if abs(num) == i:
                            final_sequence.append(num)
                            break
                else:
                    # Insert the ideal move if it's missing
                    final_sequence.append(i)

            return final_sequence
        
        else:
            return sequence

    def orderCalculation(self, sequence, length):
        """
        Calculate the points for maintaining the correct order:
        For index i in [0..length-1], compare the user’s move 
        vs. ideal_sequence[i]. Deduct points for a mismatch.
        """
        ideal_sequence = list(range(1, length + 1))
        order_points = 100.0
        penalty_per_move = 100.0 / length

        # Compare the user's (possibly extended) sequence 
        # to ideal indexes up to length
        for i, num in enumerate(sequence):
            if i >= length:
                break
            # Compare raw values, so negative placeholders also get penalized
            if abs(num) != ideal_sequence[i]:
                order_points -= penalty_per_move

        order_points = max(order_points, 0)
        return order_points


# ----------------- Main / Test code ---------------------
if __name__ == "__main__":
    length = int(input("Sequence length: "))
    sequence = input("Sequence: ")

    sequenceArray = sequence.split()
    intSequenceArray = [int(num.strip()) for num in sequenceArray]

    calculator = MimicryScoreCalculator()

    # 1) Deduction for extra moves and update sequence
    deduction, updatedSequence = calculator.extraMoveCalculation(intSequenceArray, length)

    # 2) Calculate move points after removing extras
    move_points = calculator.moveCalculation(updatedSequence, length)

    # 3) Build final sequence (append negatives if any moves are missing),
    #    but do NOT reorder the user's typed moves:
    final_sequence = calculator.completeMissingMoves(updatedSequence, length)

    # 4) Calculate order points on this final sequence
    order_points = calculator.orderCalculation(final_sequence, length)

    # 5) Final Score
    final_score = move_points + order_points - deduction

    print(f"\nMove Points: {move_points:.2f}")
    print(f"Order Points: {order_points:.2f}")
    print(f"Deduction for Extra Moves: -{deduction:.2f}")
    print(f"Full Sequence for Order Check: {final_sequence:.2f}")
    print(f"\nFinal Score: {final_score:.2f}")