% Define the base case: the sum of integers from 1 to 1 is 1.
sum_to_n(1, 1).

% Define the recursive case: the sum of integers from 1 to N is N plus the sum of integers from 1 to N-1.
sum_to_n(N, Sum) :-
    N > 1,             % Ensure that N is greater than 1 to avoid infinite recursion.
    N1 is N - 1,       % Calculate N-1.
    sum_to_n(N1, Sum1),% Recursively calculate the sum of integers from 1 to N-1.
    Sum is Sum1 + N.   % Add N to the sum of integers from 1 to N-1 to get the sum of integers from 1 to N.
