def transform_data(df):
    df.dropna()
    df.drop_duplicates()
    df.drop([
    'ISO 2-character country/territory code',
    'ISO numeric country/territory code',
    'Estimated prevalence of TB (all forms) per 100 000 population, low bound',
    'Estimated prevalence of TB (all forms) per 100 000 population, high bound',
    'Estimated prevalence of TB (all forms), low bound',
    'Estimated prevalence of TB (all forms), high bound',
    'Estimated number of deaths from TB in people who are HIV-positive, low bound',
    'Estimated number of deaths from TB in people who are HIV-positive, high bound',
    'Estimated number of deaths from TB (all forms, excluding HIV), low bound',
    'Estimated number of deaths from TB (all forms, excluding HIV), high bound',
    'Estimated incidence of TB cases who are HIV-positive per 100 000 population, low bound',
    'Estimated incidence of TB cases who are HIV-positive per 100 000 population, high bound',
    'Estimated incidence of TB cases who are HIV-positive, low bound',
    'Estimated incidence of TB cases who are HIV-positive, high bound',
    'Case detection rate (all forms), percent, low bound',
    'Case detection rate (all forms), percent, high bound',
    'Method to derive mortality estimates',
    'Estimated mortality of TB cases (all forms, excluding HIV), per 100 000 population, low bound',
    'Estimated mortality of TB cases (all forms, excluding HIV), per 100 000 population, high bound',
    'Estimated incidence (all forms) per 100 000 population, low bound',
    'Estimated incidence (all forms) per 100 000 population, high bound',
    'Estimated HIV in incident TB (percent), low bound',
       'Estimated HIV in incident TB (percent), high bound',
       'Method to derive incidence estimates',
       'Method to derive prevalence estimates',
       'Method to derive TBHIV estimates'
], axis=1, inplace=True)
    return df
    