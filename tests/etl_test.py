from ingest_system.etl import ETL
from unittest import mock
import pandas as pd
import numpy as np


@mock.patch("pandas.read_csv", return_value=pd.DataFrame())
def test_extract(pandas_mocker):
    data = ETL().extract("my_url")
    assert isinstance(data, pd.DataFrame)
    pandas_mocker.assert_called_with("my_url", sep="\t", header=None)


def test_transform():
    df = pd.DataFrame(np.random.randint(0, 100, size=(1, 61)))
    result_df = ETL().transform(df)
    assert result_df["GLOBALEVENTID"].values == df[0].values
    assert result_df["SQLDATE"].values == df[1].values
    assert result_df["EventCode"].values == df[26].values
    assert result_df["EventBaseCode"].values == df[27].values
    assert result_df["EventRootCode"].values == df[28].values
    assert result_df["ActionGeo_FullName"].values == df[52].values
    assert result_df["ActionGeo_CountryCode"].values == df[53].values
    assert result_df["ActionGeo_CountryCode"].values == df[53].values
    assert result_df["ActionGeo_Lat"].values == df[56].values
    assert result_df["ActionGeo_Long"].values == df[57].values
    assert result_df["DATEADDED"].values == df[59].values
    assert result_df["SOURCEURL"].values == df[60].values
