"""
Minimal character-level Vanilla RNN model. Written by Andrej Karpathy (@karpathy)
BSD License
"""
import numpy as np
import math
from bigramMLE2 import *
from nltk.corpus import brown

# data I/O
# data = open('input.txt', 'r').read()  # For Wiki Corpus, Where input.txt Is The Corpus File
data=" ".join(brown.words()).strip()  # For Brown Corpus
chars = list(set(data))
data_size, vocab_size = len(data), len(chars)
print 'data has %d characters, %d unique.' % (data_size, vocab_size)
char_to_ix = { ch:i for i,ch in enumerate(chars) }
ix_to_char = { i:ch for i,ch in enumerate(chars) }

# hyperparameters
hidden_size = 100 # size of hidden layer of neurons
seq_length = 25 # number of steps to unroll the RNN for
learning_rate = 1e-1

# model parameters
Wxh = np.random.randn(hidden_size, vocab_size)*0.01 # input to hidden
Whh = np.random.randn(hidden_size, hidden_size)*0.01 # hidden to hidden
Why = np.random.randn(vocab_size, hidden_size)*0.01 # hidden to output
bh = np.zeros((hidden_size, 1)) # hidden bias
by = np.zeros((vocab_size, 1)) # output bias

def lossFun(inputs, targets, hprev):
  """
  inputs,targets are both list of integers.
  hprev is Hx1 array of initial hidden state
  returns the loss, gradients on model parameters, and last hidden state
  """
  xs, hs, ys, ps = {}, {}, {}, {}
  hs[-1] = np.copy(hprev)
  loss = 0
  # forward pass
  for t in xrange(len(inputs)):
    xs[t] = np.zeros((vocab_size,1)) # encode in 1-of-k representation
    xs[t][inputs[t]] = 1
    hs[t] = np.tanh(np.dot(Wxh, xs[t]) + np.dot(Whh, hs[t-1]) + bh) # hidden state
    ys[t] = np.dot(Why, hs[t]) + by # unnormalized log probabilities for next chars
    ps[t] = np.exp(ys[t]) / np.sum(np.exp(ys[t])) # probabilities for next chars
    loss += -np.log(ps[t][targets[t],0]) # softmax (cross-entropy loss)
  # backward pass: compute gradients going backwards
  dWxh, dWhh, dWhy = np.zeros_like(Wxh), np.zeros_like(Whh), np.zeros_like(Why)
  dbh, dby = np.zeros_like(bh), np.zeros_like(by)
  dhnext = np.zeros_like(hs[0])
  for t in reversed(xrange(len(inputs))):
    dy = np.copy(ps[t])
    dy[targets[t]] -= 1 # backprop into y
    dWhy += np.dot(dy, hs[t].T)
    dby += dy
    dh = np.dot(Why.T, dy) + dhnext # backprop into h
    dhraw = (1 - hs[t] * hs[t]) * dh # backprop through tanh nonlinearity
    dbh += dhraw
    dWxh += np.dot(dhraw, xs[t].T)
    dWhh += np.dot(dhraw, hs[t-1].T)
    dhnext = np.dot(Whh.T, dhraw)
  for dparam in [dWxh, dWhh, dWhy, dbh, dby]:
    np.clip(dparam, -5, 5, out=dparam) # clip to mitigate exploding gradients
  return loss, dWxh, dWhh, dWhy, dbh, dby, hs[len(inputs)-1]

def sample(h, seed_ix, n):
  """ 
  sample a sequence of integers from the model 
  h is memory state, seed_ix is seed letter for first time step
  """
  x = np.zeros((vocab_size, 1))
  x[seed_ix] = 1
  ixes = []
  for t in xrange(n):
    h = np.tanh(np.dot(Wxh, x) + np.dot(Whh, h) + bh)
    y = np.dot(Why, h) + by
    p = np.exp(y) / np.sum(np.exp(y))
    ix = np.random.choice(range(vocab_size), p=p.ravel())
    x = np.zeros((vocab_size, 1))
    x[ix] = 1
    ixes.append(ix)
  return ixes

p = 0
mWxh, mWhh, mWhy = np.zeros_like(Wxh), np.zeros_like(Whh), np.zeros_like(Why)
mbh, mby = np.zeros_like(bh), np.zeros_like(by) # memory variables for Adagrad
smooth_loss = -np.log(1.0/vocab_size)*seq_length # loss at iteration 0
b = BigramMLE()
b.train() # For Wiki Corpus, Give As Argument The Name Of The File Which Has The Wiki Corpus In It
perplexity = []
min_perp = -1
for n in range(10001):
  # prepare inputs (we're sweeping from left to right in steps seq_length long)
  if p+seq_length+1 >= len(data) or n == 0: 
    hprev = np.zeros((hidden_size,1)) # reset RNN memory
    p = 0 # go from start of data
  inputs = [char_to_ix[ch] for ch in data[p:p+seq_length]]
  targets = [char_to_ix[ch] for ch in data[p+1:p+seq_length+1]]
  # sample from the model now and then
  if n%1000 == 0:
    sample_ix = [
      (''.join(ix_to_char[ix] for ix in sample(hprev, inputs[0], 200)))
        for _ in range(100)
    ]
    sample_ix_prob = []
    # sample_ix = map(lambda x : ''.join(ix_to_char[ix] for ix in x)
    # print '----\n %s \n----' % (sample_ix, )
    m = 10
    s = 0
    sample_ix_perp = []
    lprob = 0.0
    total_words = 1
    for i in sample_ix:
      #call bigram function, returns prob
      prob = float(b.pSent(i))
      #print(prob)
      if(prob == 0.0):
        prob = 10.0**(-5)
      lprob += math.log(prob)
      s = s+lprob
      sample_ix_perp.append((i, float(pow(2,-math.log(prob)/len(i.split())))))
      total_words += len(i.split())

    sample_ix_perp = sorted(sample_ix_perp, key = lambda x:x[1])[:len(sample_ix_perp) if len(sample_ix_perp)<10 else 10]
    #sample_ix_perp = sorted(sample_ix_perp, key = lambda x:-x[1])[:len(sample_ix_perp)]
    perplexity.append(float(pow(2,-lprob/total_words )))  
    if(perplexity[-1] < min_perp or min_perp == -1):
        min_perp = perplexity[-1]
        min_iter = n
        min_sample_perp = sample_ix_perp
  # forward seq_length characters through the net and fetch gradient
  loss, dWxh, dWhh, dWhy, dbh, dby, hprev = lossFun(inputs, targets, hprev)
  smooth_loss = smooth_loss * 0.999 + loss * 0.001
  if n % 1000 == 0: print 'iter %d, loss: %f, perplexity: %f ' % (n, smooth_loss, perplexity[n/1000]) # print progress
  if n == 10000:
        print "The iter which returned lowest perplexity value: "+str(min_iter)+" with a perplexity value of "+str(min_perp)
        print "------------------------------"
        print "Top 10 Sentences with the least perplexity"
        c = 1
        for sip in min_sample_perp:
            print "----------------------"
            print "Sentence "+str(c)
            print sip[0]
            print "-----"
            print "Perplexity value "+str(sip[1])
            c += 1
        print "------------------------------"
  # perform parameter update with Adagrad
  for param, dparam, mem in zip([Wxh, Whh, Why, bh, by], 
                                [dWxh, dWhh, dWhy, dbh, dby], 
                                [mWxh, mWhh, mWhy, mbh, mby]):
    mem += dparam * dparam
    param += -learning_rate * dparam / np.sqrt(mem + 1e-8) # adagrad update

  p += seq_length # move data pointer
  # n += 1 # iteration counter 
