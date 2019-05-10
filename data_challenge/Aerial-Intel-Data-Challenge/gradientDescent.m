function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)

% Perform gradient descent on the cost of theta, to try to minimize this value.
% Takes the given number of iterations, as well as the value given for alpha 
% and uses these for the operation.


m = length(y); % number of training examples

% matrix holding the costs as gradient descent proceeds
J_history = zeros(num_iters, 1);

%performs the descent
for iter = 1:num_iters
	
	d = pinv(m) * X'*(X*theta - y);
	theta = theta - alpha * d;
	  
    J_history(iter) = computeCost(X, y, theta);
	
end
	
end
