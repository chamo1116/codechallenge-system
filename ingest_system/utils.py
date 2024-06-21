import pandas as pd


class ETLMixin:
    def _read_csv(self, url: str) -> pd.DataFrame:
        data = pd.read_csv(url, sep="\t", header=None)
        return data

    def _maping_columns(self, data: pd.DataFrame) -> pd.DataFrame:
        new_data = pd.DataFrame()
        new_data["GLOBALEVENTID"] = data[0]
        new_data["SQLDATE"] = data[1]
        new_data["EventCode"] = data[26]
        new_data["EventBaseCode"] = data[27]
        new_data["EventRootCode"] = data[28]
        new_data["ActionGeo_FullName"] = data[52]
        new_data["ActionGeo_CountryCode"] = data[53]
        new_data["ActionGeo_CountryCode"] = data[53]
        new_data["ActionGeo_Lat"] = data[56]
        new_data["ActionGeo_Long"] = data[57]
        new_data["DATEADDED"] = data[59]
        new_data["SOURCEURL"] = data[60]
        return new_data
