# End-to-end ML with Scikit-learn pipeline

```diff
- For the latest work please check the development branch. This branch might not be up to date... 
```

## Project aim  
My aim with this project is to show how to setup an end-to-end ML project by taking advantage of scikit-learn pipeline.

A pipeline can be defined as a sequence of data processing components. These are crusial in ML systems as a lot of data needs to be manipulated and tranformed. The components are ran asynchronusly and each component pulls in a large amount of data, processes it, and spits out the result in another data store, and then some time
later the next component in the pipeline pulls this data and spits out its own output, etc. The components are fairly self-contained: the data store is the interface between the components. Be careful with the components breaking down, they can go unnoticed until much later in the pipeline.  

The data we are going to explore can be found here [California Housing Prices](https://github.com/ageron/handson-ml/tree/master/datasets/housing) from 1990.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Project steps: 

- Understand the big picutre and the research question.
- Setup the environment using Conda with yml file (check the dependencies I choose to install, you can change as you wish).  
- Get our hands dirty by exploring and understanding the data by using Dash Plotly to visualize and analyze the variables. 
- Prepare the data for ML algorithms. 
- Select and train models. 
- Fine-tune the models. 
- Present the results. 
- And finally, launch, monitor, and maintain the system.


### Framing the problem 

The important thing here is to remember the business aspect of this problem we are trying to solve. Building a predictive model is the end goal but what are the business objectives? How does the company expect to use and benefit from this model? 

*"This is important because it will determine how you frame the problem, what algorithms you will select, what performance measure you will use to evaluate your model, and how much effort you should spend tweaking it."* 

Often the results from the ML models will be used to feed other systems along with other signals (a piece of information). In this specific sample project we are interested in a real estate investment. Before continuing it is also important to understand what the current solution looks like (if there are any). For this sample project we can assume that the housing prices are currently being estimated manually. 

Now that we have an idea about the company status and the desired outcome, we need to frame the problem into **supervised, unsupervised, or reinforcement learning.** Should we define this challenge as **classification, regression task**, or somoething else? Should we use **batch learning or online learning techniques?** 

The problem at hand will fall under these following: 

- Supervised learning as we have *labeled* training examples. 
- Regression task as we want to predict a value. It is a *multivariate regression* problem as we will use multiple features to make a prediction.
- Batch learning we be used as we do not have continues incoming flow/streaming of data and that the data is small enough to fit in memory.  

*"If the data were huge, we could either split the batch learning work across multiple servers (using the MapReduce technique), or use an online learning techniques."*

### Select a performace measure 

Our next step would be to select a performace measure. As this challenge falls under a regression task, we might be interested in using the commonly selected **Root Mean Square Error (RMSE)** It measure the *standard deviation (the square root of the variance, the average of the squared deviation from the mean)* of the errors the system makes in it predictions.   

<img src="https://latex.codecogs.com/svg.latex?RMSE(X,h)=\sqrt{\frac{1}{m}\sum_{i=1}^{m}{({h({x^{(i)}})-y^{(i)}})^2}}" title="RMSE(X,h)=\sqrt{\frac{1}{m}\sum_{i=1}^{m}{({h({x^{(i)}})-y^{(i)}})^2}}" style="background-color:white"/>

The RMSE is generally fine when implementing a regression model but when one has many outliers the *Mean Absolute Error (aka average absolute deviation)* might be better to use. 

<img src="https://latex.codecogs.com/svg.latex?MAE(X,h)=\frac{1}{m}\sum_{i=1}^{m}{|{h({x^{(i)}})-y^{(i)}}}|" title="MAE(X,h)=\frac{1}{m}\sum_{i=1}^{m}{|{h({x^{(i)}})-y^{(i)}}}|" style="background-color:white"/>

However, both these equations are ways to measure the distance between two vectors: the predictions vector and the targets vector. 

### Implementation 

When I created my environment I added the Ipykernel to the yml file but somehow it did not get installed. So, I had to run the following in the terminal: 
```batch
#Activate the environment you want to install the dependency under.
conda activate "env name"
```

```batch
#Install the ipykernel dependency as root
pip install ipykernel -U --user --force-reinstall
```

Let's move on. We first need to "somehow" split the dataset into train/test sets. This step is important as we do not want to split it diffrently each time we run the program. Over time the whole dataset will get exposed to the algorithms. Now, this step can be implemented in many different ways, so here we'll just follow the example shown in the book. Remember, this sample project is for learning, not showing off our coding skills. But if you have a "better" ways to solve this, please do shout out.  

```python
# See the functions under data_prep/data_helpers.py
train_set, test_set = data.split_train_test_id(housing,0.2,'id')
strat_train_set, strat_test_set = data.stratisfied_split_train_test(housing,0.2,"income_cat")
```



## Resources    

- [Comprehensive guide to styling a github readme file](https://ellen-park.medium.com/comprehensive-guide-to-styling-a-github-readme-2df7a6db1a00)
- [mildbread readme styling](https://gist.github.com/milkbread/5795012)
- [Hands-on Machine Learning with Scikit-learn and TensorFlow by Aurélien Géron](https://upload.houchangtech.com/pdf/Hands-on_Machine_Learning.pdf)
- [Creating an environment from an environment.yml file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [Dash Plotly](https://dash.plotly.com/)

## License 

[MIT](https://choosealicense.com/licenses/mit/)