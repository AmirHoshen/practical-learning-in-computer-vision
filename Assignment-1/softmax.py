from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

epsilon = np.finfo('float').eps

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    x_size = X.shape[0]
    #print("x_size is: ",x_size)
    feature_size = W.shape[0]
    class_size = W.shape[1]
    #print("feature_size is: ",feature_size)
    for i in range(x_size):
      wx = np.zeros(W.shape[1])
      temp_dw = np.zeros_like(W)
      for j in range(class_size):
        wx[j] = np.dot(X[i],W[:,j])
      #temp = np.dot(X[i],W[:][y[i]])
      wx -= np.max(wx)
      p = np.exp(wx) / np.sum(np.exp(wx))
      for k in range(feature_size):
          temp_dw[k] = p
      temp_dw[:,y[i]] -= 1
      #print("temp_dw shape before now: ",temp_dw.shape)
      for l in range(class_size):
        for m in range(feature_size):
          temp_dw[m][l] *= X[i][m]
      #print("temp_dw shape is now: ",temp_dw.shape)
      corr_y = p[y[i]]
      loss -= np.log(corr_y)
      dW+=temp_dw
    loss += .5*reg*np.sum(W**2)
    loss = loss/x_size
    dW/=x_size
    dW += reg*W




    pass
    # Softmax Loss

    
    # Regularization
    

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    num_train = X.shape[0]
    f = X.dot(W)
    f = f - np.max(f, axis=1)[:, np.newaxis]
    loss = -np.sum(
        np.log(np.exp(f[np.arange(num_train), y]) / np.sum(np.exp(f), axis=1)))
    loss /= num_train
    loss += 0.5 * reg * np.sum(W * W)
    ind = np.zeros_like(f)
    ind[np.arange(num_train), y] = 1
    dW = X.T.dot(np.exp(f) / np.sum(np.exp(f), axis=1, keepdims=True) - ind)
    dW /= num_train
    dW += reg * W

    pass
    
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
