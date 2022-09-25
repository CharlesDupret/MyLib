import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def plot_confusion_matrix(
    x_test: np.array, y_test: np.array, *, model, coder=None, figsize=(10, 10)
) -> None:
    """Plot the correlation matrix of the test set predictions by the given model.
    :param x_test: test set
    :param y_test: labels of true test set classification
    :param model: prediction model used
    :param coder: coder used to encode labels
    :param figsize: set the size of the figure
    """
    from sklearn.metrics import confusion_matrix

    y_pred = model.predict(x_test)

    # decode labels if they are encoded
    if coder:
        y_test = coder.inverse_transform(y_test)
        y_pred = coder.inverse_transform(y_pred)

    index = np.unique(y_test)
    columns = np.unique(y_pred)

    # change shape if lables are onehot encoded
    if len(y_test.shape) != 1:
        y_test = y_test.argmax(axis=1)
        y_pred = y_pred.argmax(axis=1)

    y_true = y_test

    # build a corelation matrix as an pandas.DataFrame for used seaborn
    df_cm = pd.DataFrame(
        confusion_matrix(y_true, y_pred, normalize="true"), index=index, columns=columns
    )

    # plot correlation matrix
    plt.figure(figsize=figsize)
    sns.heatmap(df_cm, annot=True)
