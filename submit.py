import numpy as np
import sklearn
from scipy.linalg import khatri_rao

# You are allowed to import any submodules of sklearn that learn linear models e.g. sklearn.svm etc
# You are not allowed to use other libraries such as keras, tensorflow etc
# You are not allowed to use any scipy routine other than khatri_rao

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py

# DO NOT CHANGE THE NAME OF THE METHODS my_fit, my_map etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here
# For example, functions to calculate next coordinate or step length

################################
# Non Editable Region Starting #
################################
def my_fit( X_train, y0_train, y1_train ):
################################
#  Non Editable Region Ending  #
################################
    from sklearn.linear_model import LogisticRegression
    map=my_map(X_train)
    model1 = LogisticRegression()
    model1.fit(map,y0_train)

    model2=LogisticRegression()
    model2.fit(map,y1_train)

    model1_weights = model1.coef_
    model1_intercept = model1.intercept_

    model2_weights = model2.coef_
    model2_intercept = model2.intercept_
    return model1_weights, model1_intercept, model2_weights, model2_intercept


################################
# Non Editable Region Starting #
################################
def my_map( X ):
################################
#  Non Editable Region Ending  #
################################
    result = []
    for x in X:
        d = np.array([1 - 2 * c for c in x])
        n = len(d)
        feature_vector = np.ones(n)
        running_product = 1

        for i in range(n):
            running_product *= d[i]
            feature_vector[i] = running_product
        feature_vector = np.concatenate((feature_vector, x))
        result.append(feature_vector)
    return np.array(result)
