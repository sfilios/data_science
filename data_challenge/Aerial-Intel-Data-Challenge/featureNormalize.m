function [X_norm, mu, sigma] = featureNormalize(X)

X_norm = X;
mu = zeros(1, size(X, 2));
sigma = zeros(1, size(X, 2));

mu = mean(X);
sigma = std(X);

m=size (X,1);
mu_matrix = ones(m, 1) * mu;
sigma_matrix = ones(m,1)*sigma;
X_norm=X.-mu_matrix;
X_norm=X_norm./sigma_matrix;


%take the mean of each feature and normalize by taking the mean of each feature and dividing by standard deviation


end
