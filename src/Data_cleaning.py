import pandas as pd

from Script import stock_df


def number_format(value,column_name):
    if column_name == "Symbol" or column_name == "Market_cap":
        return value
    if isinstance(value,str):
        if "%" in value:
            value = value.replace("%", "")
            if value.startswith("(") and value.endswith(")"):
                value = value[1:-1]
            return float(value)
        if "," in value:
            value = value.replace(",","")
            return int(value)
        else:
            return pd.to_numeric(value,errors="coerce")
    else:
        return value

for col in stock_df.columns:
    stock_df[col] = stock_df[col].apply(lambda x: number_format(x,col))

stock_df.to_excel("Stock_data_report.xlsx",startrow=1,startcol=5, index=False)

print(f"Stock report converted to Excel")