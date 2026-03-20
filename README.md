# dear_comrade_data_science_zero_to_hero
## Setup
### python -m venv venv
### venv\Scripts\Activate.ps1

## Deep Learning

### WHAT IS THE LAYER ?
#### A layer in a deep learning model is a structure or network topology in the model's architecture, which takes information from the previous layers and then passes it to the next layer.

#### Mixing liner combination and non non-linearities allows us to model arbitrary function
#### Functions with strange and un-conventional shapes
#### Model changes from inputs that are linearly combined, resulting in outputs to inputs that are linearly combined
#### and then go through some non-linear transformation resulting in outputs.
![Layers](/images/layers.png)

### WHAT IS DEEP NET ?
#### We take input and get output, and use this output to input to another layer, until we decide to stop, that we will compare with targets
![deep net](/images/deep_net.png)
####  All the layers between input and output are called hidden layers as we don't know what happens in between is hidden
#### Stacking the layers one after the other produces DEEP NET
#### Building blocks of hidden layers are called hidden units and hidden nodes
#### In mathematical terms if h is the tensor related to the hidden layer, each hidden unit is element of that tensor
![hidden_unit](/images/hiddent_unit.png)
#### Number of units(nodes) in the layer is often referred to as WIDTH of the layer
#### We always stack layers with same width
![same_width_layer](/images/same_width_layers.png)
#### When we build model we decide width and depth, we refer these values as HYPER-PARAMETERS
![hyper_parameters](/images/depth_of_layers.png)
#### Parameters are weight(W) and Bias(b)
#### Hyper-Parameters are width, depth, learning rate
#### Parameters are derived by optimizing model
#### Hyper-Parameters are set by developer
### DIGGING INTO DEEP NET 
#### Feed inputs and then combine these inputs linearly and then add non-linearity by using linear model
#### X*B (input (1 X 8),weights(8X9)) produces 1 X 9 matrics
![deep_net_illustration](/images/deep_of_nets_illustration.png)
#### Each arrow represents mathematical transformation of certain value
#### All the arrows takes us to  first hidden layer and certain weight is added and then non-linearity is applied
![apply_non_linearity](/images/applying_non_linearity.png)
#### Applying non-linearity does not change shape of expression,it only changes linearity
#### Arrow represents weights not non-linearities 
#### How many weights can we have ?
#### Weights matrix is 8 X 9 so there are 8*9=72
![Weight_info](/images/weights_info.png)
#### 9 arrows goes out of input to hidden node
#### Each weight has two index numbers Wij (i= index of input unit,j=index of hidden unit)

#### Example W36 is applied to 3rd input X3 it is involved in calculation h6 hidden unit
![weight_mapping](images/6th_hidden_unit_calculation.png)
#### Similarly weights W16,W26,W36,W46,W56,W66,W76,W86 all computing in 6th hidden unit
#### They are linearly combined then non-linearity added to produce 6th hidden unit
![weight_mapping](images/weight_mapping.png)
#### Same way we will get all other hidden units and 1st hidden layer is ready
#### This process continues combining linearities and adding non-linearity we produce new hidden layer
#### Until we decide what should be the output layer
![final_deep_net](/images/final_deep_net.png)
#### As before, our optimization goal is finding values for weight matrices that would allow us to convert inputs into correct outputs as best as we can.
### Why do we need non-linearity after combining linearities
![non_linearity_after_linearity](/images/non_linearity_after_linearity.png)
#### Non-Linearity is needed so we can break the linearity and represent more complicated relationships
![non_linearity_after_linearity_ans](/images/non_linearity_after_linearity_ans.png)
#### Important consequence of including non-linearity is the ability to stack layers
#### Stacking layers is the process of placing one layer after another layer in meaningful way
#### We can't stack layers when we only have liner relationships 
#### The point we will make is that we cannot stack layers when we have only linear relationships.

#### Let's prove it. Imagine we have a single hidden layer and there are no non-linearities.
#### So, our picture looks this way.
![Step_1](/images/non_linear_purpose_step_1.png)
#### There are eight input nodes,nine hidden nodes in the hidden layer and four output nodes.
#### Therefore, we have an 8 x 9 weights matrix for the linear relationship between the input layer and the hidden layer.
#### Let's call this matrix w1 and the hidden units h.
#### According to the linear model, h is equal to x times w1.
![Step_2](/images/non_linear_purpose_step_2.png)
#### Let's ignore the biases for a while.So,our hidden units are summarized in the matrix h with a shape of one by nine.
#### Now, let's get to the output layer from the hidden layer.
#### Once again, according to the linear model, y is equal to h times w2, We have w2, as these weights are different.
![Step_3](/images/non_linear_purpose_step_3.png)
#### We already know the h matrix is equal to x times w1, right?
![Step_4](/images/non_linear_purpose_step_4.png)
#### Let's replace h in this equation. y is equal to x times w1 times w2.
![Step_5](/images/non_linear_purpose_step_5.png)
#### But w1 and w2 can be multiplied, right? 
#### What we get is a combined matrix. w* with dimensions eight by four.
![Step_6](/images/non_linear_purpose_step_6.png)
#### Well then, our deep neck can be simplified into a linear model, which looks this way.
#### y equals x times w*.
#### Knowing that, we realize the hidden layer is completely useless in this case.
#### We can just train this simple linear model and we would get the same result.
![Step_7](/images/non_linear_purpose_step_7.png)
#### In mathematics, this seems like an obvious fact, but in machine learning, it is not so clear from the beginning.
#### The two consecutive linear transformations are equivalent to a single one.
#### Even if we add 100 layers the problem would be simplified to a single transformation.
![Step_8](/images/non_linear_purpose_step_8.png)
#### That is the reason we need non-linearities.
#### Without them, stacking layers, one after the other is meaningless, and without stacking layers,we will have no depth.
#### What's more, with no depth, each and every problem will equal the simple linear example we did earlier, and many practitioners would tell you it was borderline machine learning.
![Step_8](/images/non_linear_purpose_step_10.png)
#### With this we can conclude  `TO HAVE DEEEP NETS AND FIND COMPLEX RELASHANSHIPS THROUGH ORBITARY FUNCTIONS, WE NEED NON_LINEARITIES`

### ACTIVATION FUNCTIONS
#### In machine learning context non-linearities are called ACTIVATION FUNCTION
#### Activation functions transforms inputs into outputs of different kind
![activation_function](/images/activation_function.png)
#### Example brain / body experience change in temperature suggest you to weare cote or not  
![activation_function](/images/activation_function_example_1.png)
#### Different type of activation functions
![types_of_activation_fns](/images/type_of_activation_funs.png)
#### Activation functions are also called TRANSFER FUNCTIONS
### Activation Functions: SOFTMAX 
#### Softmax function does not have definite graph
#### Softmax function takes as argument the whole vector a
#### Softmax considers the information from whole matrix
#### So the softmax function is equal to the exponential of the element at position I divided by the sum of the exponential of all elements of the vector.
#### So while the other activation functions get an input value and transform it regardless of the other elements, the softmax considers the information about the whole set of numbers we have.
#### Time for an example.
#### Let a be equal to xw plus b, which is our well-known model, then we can say the output of y will be the softmax of a.
#### Let's look at a hidden layer with three units, so a here is equal to hw plus b.
##### After transforming it through a linear combination, we obtain a vector a with three elements  [-0.21, 0.47, 1.72.]
![softmax_step_1](/images/softmax_step_1.png)
#### Now, if we used a different activation such as the sigmoid, we would simply apply the formula for each of the three numbers, and we would obtain a new vector containing three new numbers.
#### But softmax is special. Each element in the output depends on the entire set of elements of the input.
#### Let's find the softmax of a. First, I'll calculate the denominator.
#### It is given by e to the power of minus 0.21 plus e to the power of 0.47 plus e to the power of 1.72. That's approximately eight.
#### Then we must divide each exponential by this denominator to get the new vector.
#### The result is 0.1, 0.2, and 0.7. This is our output layer.
![softmax_step_2](/images/softmax_step_2.png)

#### A key aspect of the softmax transformation is that the values it outputs are in the range (0, 1).
#### Their sum is exactly one.
#### Probabilities has similar properties.
#### The point of the softmax transformation is to transform a bunch of arbitrarily large or small numbers that come out of previous layers and fit them into a valid probability distribution.
#### This is extremely important and useful.
![softmax_step_3](/images/softmax_step_3.png)
#### Remember our example with cats, dogs, and horses we saw earlier?
#### One photo was described by a vector containing 0.1, 0.2, and 0.7.
#### We promised we will tell you how to do that. Well, that's how, through a softmax transformation. We kept our promise.
#### Now that we know we are talking about probabilities, we can comfortably say we are 70% certain
![softmax_step_4](/images/softmax_step_4.png)
#### the image is a picture of a horse. This makes everything so intuitive and useful that the softmax activation is often used as the activation of the final output layer in classification problems.
#### So no matter what happens before, the final output of the algorithm is a probability distribution.


### Back Propagation
![back_propagation_step_0](/images/back_propagation_step_0.png)
#### that the training process consists of updating parameters through the gradient descent for optimizing the objective function.
![back_propagation_step_1](/images/back_propagation_step_1.png)
#### In supervised learning, the process of optimization consisted of minimizing the loss.
#### Our updates were directly related to the partial derivatives of the loss and indirectly related to the errors, or deltas as we called them.
#### The deltas were the differences between the targets and the outputs.
#### deltas for the hidden layers are trickier to define, still, they have a similar meaning.
#### The procedure for calculating them is called backpropagation of errors.
#### Having these deltas allows us to vary parameters using the familiar update rule.
![back_propagation_step_2](/images/back_propagation_step_2.png)
### Forward Propagation
#### Forward propagation is the process of pushing inputs through the net.
#### At the end of each epoch, the obtained outputs are compared to the targets to form the errors.
![back_propagation_step_3](/images/back_propagation_step_3.png)
#### Then we backpropagate through partial derivatives and change each parameter so errors at the next epoch are minimized.
![back_propagation_step_4](/images/back_propagation_step_4.png)
#### For the minimal example, the backpropagation consisted of a single step aligning the weights given the errors we obtained. 
#### Here's where it gets a little tricky.
#### When we have a deep net, we must update all the weights related to the input layer and the hidden layers.
![back_propagation_step_5](/images/back_propagation_step_5.png)
#### For example, in this famous picture, we have 270 weights, and yes, this means we had to manually draw all 270 arrows
#### you see here.
![back_propagation_step_6](/images/back_propagation_step_6.png)
#### So, updating all 270 weights is a big deal. But wait, we also introduced activation functions.
#### This means we have to update the weights accordingly considering the used non-linearities and their derivatives.
#### Finally, to update the weights we must compare the outputs to the targets.
#### This is done for each layer but we have no targets for the hidden units.
#### We don't know the errors, so how do we update the weights? That's what backpropagation is all about.
#### We must derive the appropriate updates as if we had targets.
![back_propagation_step_7](/images/back_propagation_step_7.png)
#### Now, the way academics solve this issue is through errors.
#### The main point is that we can trace the contribution of each unit, hidden or not, to the error of the output.
![back_propagation_step_8](/images/back_propagation_step_8.png)

### Backpropagation Picture
#### Let's look at the schematic illustration of backpropagation shown here.
#### Our net is quite simple.
#### It has a single hidden layer. Each note is labeled, so we have inputs x1 and x2.
#### Hidden layer units, output layer units, y1 and y2.
#### And finally, the targets t1 and t2.
![back_propagation_step_9](/images/back_propagation_step_9.png)
#### The weights are W11, W12, W13, W21, W22, and W23, for the first part of the net.
#### For the second part, we name them U11, U12, U21, U22, U31, and U32.
#### So we can differentiate between the two types of weights.
#### We know the error associated with y1 and y2,as it depends on known targets.
#### So, let's call the two errors, e1 and e2.
#### Based on them, we can adjust the weights labeled with U. Each U contributes to a single error.
![back_propagation_step_10](/images/back_propagation_step_10.png)
#### For example, u11 contributes to e1. Then, we find it's derivative and update the coefficient.
#### Nothing new here. Now, let's examine w11.
#### w11 helped us predict h1, but then, we needed h1 to calculate y1 and y2. Thus, it played a role in determining both errors, e1 and e2.
![back_propagation_step_11](/images/back_propagation_step_11.png) 
#### So, while u11 contributes to a single error, w11 contributes to both errors.
#### Therefore, its adjustment rule must be different. The solution to this problem is to take the errors, and backpropagate them through the net, using the weights.
#### Knowing the U weights,we can measure the contribution of each hidden unit to the respective errors.
#### Then, once we found out the contribution of each hidden unit to the respective errors, we can update the W weights.
#### So essentially, through backpropagation, the algorithm identifies which weights lead to which errors.
#### Then, it adjusts the weights that have a bigger contribution to the errors by more than the weights, with a smaller contribution.
![back_propagation_step_12](/images/back_propagation_step_12.png) 
#### A big problem arises when we might also consider the activation functions.
#### They introduce additional complexity to this process.
#### Linear contributions are easy, but non-linear ones are tougher.
![back_propagation_step_13](/images/back_propagation_step_13.png) 
#### Imagine backpropagating in our introductory net. Once you understand it, it seems very simple.
#### While pictorially straightforward, mathematically it is rough, to say the least.
![back_propagation_step_14](/images/back_propagation_step_14.png) 

### Over fitting
#### Our training has focused on the particular training set so much, it has missed the point.
### Under fitting
#### Model has not captured the under laying logic of the data.

### Training
#### Where training takes place
### Validation
#### Help us to prevent over fitting
#### All the training done on the training set,
![training_set](/images/training_set.png)
#### We update weights and bias for training set only
#### Every once in while we stop training a bit, at this point model is somewhat trained
![some_what_trained](/images/some_what_trained.png)
#### Take the model apply it to the validation dataset
#### This time we will run it without applying weights, only propagate forward not backward. 
#### We will just calculate lose function, on average it should be equals to training set
![training_loss_function_validation](/images/training_loss_function_validation.png)
#### Training and validation data sets are derived from same source
![training_validation_data_set](/images/training_validation_data_set.png)
#### We will perform this operation many times
#### Two loss functions we calculate are referred to training loss, validation loss
#### Data in the training set trained set using gradient descent
#### Each subsequent loss less or equal to previous loss
![training_validation_loss](/images/training_validation_loss.png)
#### At some point validation loss start increasing, that is red flag
#### We are overfitting, we are getting better at predicting, but loosing overall logic data
#### At this point we stop training model
![over_fitting](/images/training_overfitting.png)
#### We update weight and bias for training set 
#### Training set and validation set should not be overlapped 
#### Data set is separated into three, Training, Validation, Test set
![training_validation_test](/images/training_validation_test.png)
#### We need to run the data set it has not seen.
![training_validation_test_1](/images/training_validation_test_1.png)
### Test
#### The accuracy we get by forward propagating the test dataset, is the accuracy we expect the model to have if we deploy in the real life. 
#### 80% training, 10% validation, 10% test ratio
#### 70% training, 20% validation, 10% test ratio
#### Training set always greater than other sets
#### We train the model using training set only
![training_and_validation_phase](/images/training_and_validation_phase.png)
#### Every now and then we validate data set by running validation dataset
![validate_now_and_then](/images/validate_now_and_then.png)
#### Usually we validate on evry epoch 
#### We always calculate training_loss , validation_loss
#### if training_loss and validation_loss goes hand in hand nothing to move along
#### validation_loss is increasing that means we are overfitting the model.
#### Test the model with test data set using forward propagation
#### Accuracy obtained in this step is accuracy of the model.
### N-Fold cross validation
#### What if can not split the dataset, if we split dataset model may not be able learn any relationship between data
![can_not_split](/images/can_not_split.png)
#### N-Fold cross validation is a strategy which combines training and validation dataset in clever way.
![n_fold_cross_validation](/images/n_fold_cross_validation.png)
#### it still requires test dataset.
![10_fold_cross_validation](/images/10_fold_cross_validation.png)
#### If we have 11000 records, initially split it to 10000(Training + Validation), 1000 (test)
#### Split to 10 chunks 9 are training and 1 is validation, this is called 10-fold cross validation.
#### make it to 10 folds and change the validation chunk on each epoch
![10_fold_cross_validation_step_1](/images/10_fold_cross_validation_step_1.png)
![n_fold_pros_cons](/images/n_fold_pros_cons.png)
### When to stop training model
#### We train the model until loss function is minimized.
#### EARLY STOPPING is technique to stop over fitting
![early_stopping](/images/early_stopping.png)
#### TRAIN ONLY FOR PRESET NUMBER OF EPOCHE
![early_stopping_approach_1](/images/early_stopping_approach_1.png)
#### STOP WHEN LOSS FUNCTION UPDATES BECOMES TOO SMALL
#### stop when loss function becomes 0.001
#### The loss function stop changing, making the update rule yield same weights.
#### We save computing power by using few iterations as possible, we don't iterate uselessly.
![stop_updating_on_to_small_loss_fn](/images/stop_updating_on_to_small_loss_fn.png)
### VALIDATION SET strategy
![validation_set_strategy](/images/validation_set_strategy.png)
#### Comparison 
![stop_training_comparision](/images/stop_training_comparision.png)

### INITIALIZATION
#### Initialization is process in which we set the initial values of weight
#### Let us initialize weights and biases in a such way that they are equal to constant.
![initialization_basic](/images/initialization_basic.png)
#### The three hidden units are symetrical w.r.t inputs
![initialization_symetric](images/initialization_symetric.png)
#### With equal inputs there is nothing to learn 
![initialization_nothing_to_learn](/images/initialization_nothing_to_learn.png)
#### Some optimization still take place, still weights remain useless.
#### Each value has an equal probability of being selected.
### Problem
![problem_statement](images/problem_statement.png)
#### Let's explore the problem. 
#### Weights are used in linear combinations. Then the linear combinations are activated.
#### Once more, we will use the sigmoid activator.The sigmoid, as other commonly used non-linearities,is peculiar around its mean and its extremes.
#### Activation functions take as inputs the linear combination of the units from the previous layer, right? Well, if the weights are too small, this will cause values that fall around this range.
#### In this range, unfortunately, the sigmoid is almost linear.
#### If all our inputs are in this range, which will happen if we use small weights, the sigmoid would not apply a non-linearity but a linearity to the linear combination.
![sigmoid_linear](images/sigmoid_linear.png)
#### Non-linearities are essential for deep nets.
#### Conversely, if the values are too large or too small, the sigmoid is almost flat, which causes the output of the sigmoid to be only once or only zeros, respectively.


### Xavier Initialization
#### Main Idea: method is not so important, number INPUTS and OUTPUTS are
![xavier_initialization](images/xavier_initialization.png)
#### Why inputs and output matters
#### That's where the activation function is going. So the higher number of outputs the higher need to spread weights.
#### optimization is done through back propagation. So when we back propagate, we would obviously have the same problem, but in the opposite direction.

### Momentum 
![momentum_step_1](images/momentum_step_1.png)
#### How do we add momentum to model
![momentum_step_2](images/momentum_step_2.png)
#### The best way to check how past the ball rolls, is to check how fast it rolled a moment ago
![momentum_step_3](images/momentum_step_3.png)
![momentum_step_4](images/momentum_step_4.png)
#### hyperparameter
![momentum_step_5](images/momentum_step_5.png)

#### 
### Learning Rate
![learning_rate_step_1](images/learning_rate_step_1.png)
![learning_rate_step_2](images/learning_rate_step_2.png)
![learning_rate_step_3](images/learning_rate_step_3.png)
![learning_rate_step_4](images/learning_rate_step_4.png)
![learning_rate_step_5](images/learning_rate_step_5.png)
![learning_rate_step_6](images/learning_rate_step_6.png)
![learning_rate_step_7](images/learning_rate_step_7.png)
![learning_rate_step_8](images/learning_rate_step_8.png)
![learning_rate_step_9](images/learning_rate_step_9.png)















[LLMs from Scratch – Practical Engineering from Base Model to PPO RLHF](https://www.youtube.com/watch?v=p3sij8QzONQ)

[Data set-1](https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope)

[Machine Learning for Everybody – Full Course](https://www.youtube.com/watch?v=i_LwzRVP7bg&list=PLWKjhJtqVAblStefaz_YOVpDWqcRScc2s&index=1)
[Vector 3D](https://academo.org/demos/3d-vector-plotter/)