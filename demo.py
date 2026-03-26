import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# load data
df = pd.read_csv(r"C:\Users\DELL\Desktop\BICY_Veg_RoadTransect_Cleaned_PUBLIC_usa.csv")

# clean columns
df.columns = df.columns.str.strip()

print("Columns:", df.columns)

# try to detect date column automatically
date_col = None
for col in df.columns:
    if "date" in col.lower():
        date_col = col
        break

if date_col:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df["Month"] = df[date_col].dt.to_period("M").astype(str)
else:
    df["Month"] = "All"

# create fake columns if not exist (dashboard safe)
if "Sales" not in df.columns:
    df["Sales"] = 1

if "Profit" not in df.columns:
    df["Profit"] = 1

if "Region" not in df.columns:
    df["Region"] = "All"

if "Category" not in df.columns:
    df["Category"] = "All"

if "Segment" not in df.columns:
    df["Segment"] = "All"

if "State" not in df.columns:
    df["State"] = "All"

if "Sub-Category" not in df.columns:
    df["Sub-Category"] = "All"

if "Discount" not in df.columns:
    df["Discount"] = 0

if "Quantity" not in df.columns:
    df["Quantity"] = 1

if "Ship Mode" not in df.columns:
    df["Ship Mode"] = "Standard"

if "Order ID" not in df.columns:
    df["Order ID"] = range(len(df))


app = dash.Dash(__name__)

app.layout = html.Div([

html.H1("ADVANCED DASHBOARD", style={'textAlign':'center'}),

html.Div([
    dcc.Dropdown(
        options=[{"label": i, "value": i} for i in df["Region"].unique()],
        value=df["Region"].unique()[0],
        id="region-filter"
    )
]),

html.Div(id="kpi-cards"),

html.Div([
    dcc.Graph(id="sales-category"),
    dcc.Graph(id="profit-segment"),
], style={'display':'flex'}),

dcc.Graph(id="monthly-trend"),

html.Div([
    dcc.Graph(id="region-sales"),
    dcc.Graph(id="top-products"),
], style={'display':'flex'}),

dcc.Graph(id="scatter"),

html.Div([
    dcc.Graph(id="sales-region"),
    dcc.Graph(id="profit-category"),
], style={'display':'flex'}),

html.Div([
    dcc.Graph(id="ship-mode"),
    dcc.Graph(id="bubble-chart"),
], style={'display':'flex'}),

dcc.Graph(id="region-monthly"),

])


@app.callback(
[
Output("kpi-cards","children"),
Output("sales-category","figure"),
Output("profit-segment","figure"),
Output("monthly-trend","figure"),
Output("region-sales","figure"),
Output("top-products","figure"),
Output("scatter","figure"),
Output("sales-region","figure"),
Output("profit-category","figure"),
Output("ship-mode","figure"),
Output("bubble-chart","figure"),
Output("region-monthly","figure"),
],
Input("region-filter","value")
)

def update(region):

    dff = df[df["Region"]==region]

    total_sales = dff["Sales"].sum()
    total_profit = dff["Profit"].sum()
    orders = dff["Order ID"].nunique()

    kpi = html.Div([
        html.Div([html.H4("Sales"), html.H2(f"{total_sales:,.0f}")]),
        html.Div([html.H4("Profit"), html.H2(f"{total_profit:,.0f}")]),
        html.Div([html.H4("Orders"), html.H2(orders)])
    ], style={'display':'flex','justifyContent':'space-around'})

    sales_category = px.bar(
        dff.groupby("Category")["Sales"].sum().reset_index(),
        x="Category", y="Sales", color="Category"
    )

    profit_segment = px.pie(
        dff.groupby("Segment")["Profit"].sum().reset_index(),
        names="Segment", values="Profit"
    )

    monthly = px.line(
        dff.groupby("Month")["Sales"].sum().reset_index(),
        x="Month", y="Sales"
    )

    region_sales = px.bar(
        dff.groupby("State")["Sales"].sum().reset_index(),
        x="State", y="Sales"
    )

    top_products = px.bar(
        dff.groupby("Sub-Category")["Sales"].sum().reset_index(),
        x="Sub-Category", y="Sales"
    )

    scatter = px.scatter(
        dff, x="Discount", y="Profit", size="Sales", color="Category"
    )

    sales_region = px.pie(
        dff.groupby("Region")["Sales"].sum().reset_index(),
        names="Region", values="Sales"
    )

    profit_category = px.bar(
        dff.groupby("Category")["Profit"].sum().reset_index(),
        x="Category", y="Profit", color="Category"
    )

    ship_mode = px.bar(
        dff.groupby("Ship Mode")["Sales"].sum().reset_index(),
        x="Ship Mode", y="Sales"
    )

    bubble = px.scatter(
        dff, x="Sales", y="Profit", size="Quantity", color="Category"
    )


    monthly_region = px.line(
        dff.groupby(["Month","Region"])["Sales"].sum().reset_index(),
        x="Month", y="Sales", color="Region"
    )


    return (kpi, sales_category, profit_segment, monthly,
            region_sales, top_products, scatter,
            sales_region, profit_category,
            ship_mode, bubble, monthly_region)


if __name__ == "__main__":
    app.run(debug=True)