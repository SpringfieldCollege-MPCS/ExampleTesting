# Example Testing

First things first: create a conda virtual environment!

1. `conda create -n exampletesting python=3.9`
2. `conda activate exampletesting`

Now that we have a virtual environment we now "install" our package

1. `pip install -e .` - This will install the package here in "development mode". This means we wont have to constantly keep reinstalling if we make changes.  This is way of installing only makes sense if you plan to make changes, which we will on this one!

Executing the above command should have installed `pytest` for us. Lets try it out and see if it works!