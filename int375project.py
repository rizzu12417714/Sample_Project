import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# load data
df = pd.read_csv(r"C:\C++ vs code\.vscode\projectdata.csv", sep="\t")

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

app = dash.Dash(__name__)

app.layout = html.Div([

html.H1("SUPERSTORE SALES ADVANCED DASHBOARD",
style={'textAlign':'center'}),

# FILTER
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

# NEW
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

    # KPI
    total_sales = dff["Sales"].sum()
    total_profit = dff["Profit"].sum()
    orders = dff["Order ID"].nunique()

    kpi = html.Div([
        html.Div([html.H4("Sales"), html.H2(f"${total_sales:,.0f}")]),
        html.Div([html.H4("Profit"), html.H2(f"${total_profit:,.0f}")]),
        html.Div([html.H4("Orders"), html.H2(orders)])
    ], style={'display':'flex','justifyContent':'space-around'})

    # charts
    sales_category = px.bar(
        dff.groupby("Category")["Sales"].sum().reset_index(),
        x="Category", y="Sales", color="Category",
        title="Sales by Category"
    )

    profit_segment = px.pie(
        dff.groupby("Segment")["Profit"].sum().reset_index(),
        names="Segment", values="Profit",
        title="Profit by Segment"
    )

    monthly = px.line(
        dff.groupby("Month")["Sales"].sum().reset_index(),
        x="Month", y="Sales", markers=True,
        title="Monthly Trend"
    )

    region_sales = px.bar(
        dff.groupby("State")["Sales"].sum().reset_index().nlargest(10,"Sales"),
        x="State", y="Sales",
        title="Top States by Sales"
    )

    top_products = px.bar(
        dff.groupby("Sub-Category")["Sales"].sum().reset_index(),
        x="Sub-Category", y="Sales",
        title="Sub Category Sales"
    )

    scatter = px.scatter(
        dff,
        x="Discount",
        y="Profit",
        size="Sales",
        color="Category",
        title="Discount vs Profit"
    )

    # NEW GRAPHS
    sales_region = px.pie(
        dff.groupby("Region")["Sales"].sum().reset_index(),
        names="Region",
        values="Sales",
        hole=.5,
        title="Sales by Region"
    )

    profit_category = px.bar(
        dff.groupby("Category")["Profit"].sum().reset_index(),
        x="Category",
        y="Profit",
        color="Category",
        title="Profit by Category"
    )

    ship_mode = px.bar(
        dff.groupby("Ship Mode")["Sales"].sum().reset_index(),
        x="Ship Mode",
        y="Sales",
        color="Ship Mode",
        title="Ship Mode Sales"
    )

    bubble = px.scatter(
        dff,
        x="Sales",
        y="Profit",
        size="Quantity",
        color="Category",
        title="Sales vs Profit Bubble"
    )

    monthly_region = px.line(
        dff.groupby(["Month","Region"])["Sales"].sum().reset_index(),
        x="Month",
        y="Sales",
        color="Region",
        title="Region Wise Monthly Sales"
    )

    return (kpi, sales_category, profit_segment, monthly,
            region_sales, top_products, scatter,
            sales_region, profit_category,
            ship_mode, bubble, monthly_region)


if __name__ == "__main__":
    app.run(debug=True)