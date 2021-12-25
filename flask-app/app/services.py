
__required = ['MSSubClass',
              'MSZoning',
              'LotArea',
              'Street',
              'LotShape',
              'LandContour',
              'Utilities',
              'LotConfig',
              'LandSlope',
              'Neighborhood',
              'Condition1',
              'Condition2',
              'BldgType',
              'HouseStyle',
              'OverallQual',
              'OverallCond',
              'YearBuilt',
              'YearRemodAdd',
              'RoofStyle',
              'RoofMatl',
              'Exterior1st',
              'Exterior2nd',
              'MasVnrType',
              'MasVnrArea',
              'ExterQual',
              'ExterCond',
              'Foundation',
              'BsmtQual',
              'BsmtCond',
              'BsmtExposure',
              'BsmtFinType1',
              'BsmtFinSF1',
              'BsmtFinType2',
              'BsmtFinSF2',
              'BsmtUnfSF',
              'TotalBsmtSF',
              'Heating',
              'HeatingQC',
              'CentralAir',
              'Electrical',
              '1stFlrSF',
              '2ndFlrSF',
              'LowQualFinSF',
              'GrLivArea',
              'BsmtFullBath',
              'BsmtHalfBath',
              'FullBath',
              'HalfBath',
              'BedroomAbvGr',
              'KitchenAbvGr',
              'KitchenQual',
              'TotRmsAbvGrd',
              'Functional',
              'Fireplaces',
              'GarageType',
              'GarageYrBlt',
              'GarageFinish',
              'GarageCars',
              'GarageArea',
              'GarageQual',
              'GarageCond',
              'PavedDrive',
              'WoodDeckSF',
              'OpenPorchSF',
              'EnclosedPorch',
              '3SsnPorch',
              'ScreenPorch',
              'PoolArea',
              'MiscVal',
              'MoSold',
              'YrSold',
              'SaleType',
              'SaleCondition']


def check_required_features(data: dict):
    """function to check that all the features required for prediction are present

    Args:
        data (dict): [features user sended]

    Raises:
        Exception: [if some feature not found]
    """

    features = data.keys()

    for feature in features:
        if feature not in __required:
            raise Exception(
                f'some feature not found. feature required is {__required}')


def get_data_of_features(data: dict):
    """function to extract value from request

    Args:
        data (dict): [json request contain the features and values]

    Returns:
        [list]: [contain values only without the features]
    """

    return list(data.values())
