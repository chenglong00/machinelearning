

class RecommenderException(Exception):
    """
    Recommender base exception. Handled at the outermost level.
    All other exception types are subclasses of this exception type.
    """


class OperationalException(RecommenderException):
    """
    Requires manual intervention and will stop the service.
    Most of the time, this is caused by an invalid Configuration.
    """


class DependencyException(RecommenderException):
    """
    Indicates that an assumed dependency is not met.
    This could happen when there is currently not enough money on the account.
    """


class DataError(RecommenderException):
    """
    Errors with data validation.
    Usually caused by errors in the data.
    """

class ModelError(RecommenderException):
    """
    Errors with model training and prediction.
    Usually caused by errors in the model.
    """