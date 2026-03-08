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















[LLMs from Scratch – Practical Engineering from Base Model to PPO RLHF](https://www.youtube.com/watch?v=p3sij8QzONQ)

[Data set-1](https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope)

[Machine Learning for Everybody – Full Course](https://www.youtube.com/watch?v=i_LwzRVP7bg&list=PLWKjhJtqVAblStefaz_YOVpDWqcRScc2s&index=1)
[Vector 3D](https://academo.org/demos/3d-vector-plotter/)