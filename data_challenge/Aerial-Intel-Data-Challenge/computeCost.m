function J = computeCost(X, y, theta)

%computes the cost of a given theta using linear regression
m = length(y); % number of training examples

J = 0;

J = (X*theta-y).^2;

J = pinv(2*m)*sum(J);


end
