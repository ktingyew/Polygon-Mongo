from controllers.polygon import PolygonParams, POLYGON_KEY, polygon_agg_call, polygon_clean_json
from controllers.unixtime import get_time_NY, get_time_SG, fmt
from datetime import timedelta

from controllers.mongo import MONGOCOL

ticker = "AAPL"

params = PolygonParams( ticker, 
                        "1",
                        "hour", 
                        (get_time_NY() - timedelta(days=3)).strftime("%Y-%m-%d"),
                        get_time_NY().strftime("%Y-%m-%d"),
                        "false",
                        "asc",
                        "50000",
                        POLYGON_KEY)

x = polygon_agg_call(params)
x['timestamp_sg'] = get_time_SG().strftime(fmt)
x['timestamp_ny'] = get_time_NY().strftime(fmt)

print(x)

MONGOCOL.insert_one(x)